#include <iostream> 
#include <chrono> 
#include <thread> 
#include <opencv2/opencv.hpp>
#include <msg.pb.h>

#include <zmq.hpp>

zmq::context_t m_context;
zmq::socket_t m_socket; 

void connect(int port){
	m_context = zmq::context_t(1);
	m_socket = zmq::socket_t(m_context, zmq::socket_type::req); 

	m_socket.connect("tcp://localhost:" + std::to_string(port));
	if (!m_socket.connected()){
		std::cout << "Unable to start server" << std::endl;
		std::runtime_error("Unable to start server");
	}
	std::cout << "Connect" << std::endl;
}

void publishFrame(const std::string &data){
	std::cout<<"PublishFrame"<< std::endl;
	zmq::message_t payload(data.size()); 

	memcpy((void *)payload.data(), data.c_str(), data.size()); 
	try{
        	auto rc = m_socket.send(payload, zmq::send_flags::none);
    	}
    	catch(zmq::error_t& e)
    	{
        	//spdlog::error(e.what());
        	std::cout<<"error"<<e.what()<<std::endl;
    	}


    	zmq::message_t z_in;
    	m_socket.recv(z_in);
}

void produceForBroadCast(){
	std::cout << "produceForBroadcast"<<std::endl; 
	cv::VideoCapture cap(0);

	if (!cap.isOpened()){
		std::cout<<"unable to open capture device"<<std::endl;
		return;
	}
	cv::Mat frame; 

	cv::namedWindow("video feed", cv::WINDOW_AUTOSIZE);
	while (cap.get(cv::CAP_PROP_POS_FRAMES) != cap.get(cv::CAP_PROP_FRAME_COUNT) - 1){
		cap.read(frame);
		std::cout << "packer" << std::endl; 

		RL::OcvMat serializableMat;
		serializableMat.set_rows(frame.rows);
        	serializableMat.set_cols(frame.cols);
        	serializableMat.set_channels(frame.channels());
        	serializableMat.set_elt_type(frame.type());
        	serializableMat.set_elt_size((int)frame.elemSize());
        	size_t dataSize  = frame.rows * frame.cols * frame.elemSize();
        	serializableMat.set_mat_data(frame.data, dataSize);

		std::string encoded_msg; 
		serializableMat.SerializeToString(&encoded_msg);

		publishFrame(encoded_msg);

	}

	cv::destroyAllWindows();

	return;
}


int main(){
connect(5000);
produceForBroadCast();
return 0;
}

