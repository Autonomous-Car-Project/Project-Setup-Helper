import argparse 
import logging 
import coloredlogs 
import numpy as np 
import os 
import cv2 


def quat2rot(quats):
  quats = np.array(quats)
  input_shape = quats.shape
  quats = np.atleast_2d(quats)
  Rs = np.zeros((quats.shape[0], 3, 3))
  q0 = quats[:, 0]
  q1 = quats[:, 1]
  q2 = quats[:, 2]
  q3 = quats[:, 3]
  Rs[:, 0, 0] = q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3
  Rs[:, 0, 1] = 2 * (q1 * q2 - q0 * q3)
  Rs[:, 0, 2] = 2 * (q0 * q2 + q1 * q3)
  Rs[:, 1, 0] = 2 * (q1 * q2 + q0 * q3)
  Rs[:, 1, 1] = q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3
  Rs[:, 1, 2] = 2 * (q2 * q3 - q0 * q1)
  Rs[:, 2, 0] = 2 * (q1 * q3 - q0 * q2)
  Rs[:, 2, 1] = 2 * (q0 * q1 + q2 * q3)
  Rs[:, 2, 2] = q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3

  if len(input_shape) < 2:
    return Rs[0]
  else:
    return Rs

# Loading Parser
parser = argparse.ArgumentParser(description='SANDS OF TIME DATA CREATOR')
parser.add_argument('-f',"--file", required=True, help="Enter the Hash Folder name")
args = parser.parse_args()

# Loading logger
logger = logging.getLogger(__name__)   # TYPES OF LOGGING: debug info warning error critical
coloredlogs.install(level='DEBUG', logger=logger)

# Basic Information
logger.info("SANDS OF TIME DATA COLLECTOR")
logger.info("v1.0")
logger.info(f"Folder Name: {args.file}")

# Creating Folder to save results 
try:
    output_file_name = f"{args.file}".split("_")[0]
    img_dir = output_file_name + "/img"
    pose_dir = output_file_name + "/pose_processed"
    os.makedirs(img_dir)
    os.makedirs(pose_dir)
except FileExistsError:
    img_dir = output_file_name + "/img"
    pose_dir = output_file_name + "/pose_processed"
    logger.warning("Output File Exists Already! Existing files mights get Overwritten!")


folders = os.listdir(args.file)
internal_folders = sorted([int(folder) for folder in folders]) 
logger.info(f"Toltal Number of Folders: {len(internal_folders)}  [{internal_folders[0]} - {internal_folders[-1]}]")

global_frame_counter = 0

for folder_num, internal_folder in enumerate(internal_folders):
    folder_dir = f"{args.file}/{str(internal_folder)}/"
    video_file = folder_dir+"video.hevc"
    logger.info(f"({folder_num + 1}/{len(internal_folders)}) Processing {video_file} ...")
    video = cv2.VideoCapture(video_file)
    num_frame = 0 
    while True:
        ret, _ = video.read()
        if not ret:
            break 
        num_frame += 1
    logger.info(f"Number of Frame in {args.file}/{str(internal_folder)} : {num_frame}")
    video = cv2.VideoCapture(video_file)
    frame_positions_path = folder_dir + "global_pose/frame_positions"
    frame_orientations_path = folder_dir + "global_pose/frame_orientations"
    
    logger.info("Reading frame positions and orientations...")
    frame_positions = np.load(frame_positions_path)
    frame_orientations = np.load(frame_orientations_path)
    if len(frame_orientations) == len(frame_positions):
        logger.info("Frame Position and Orientation READ")
    else:
        logger.critical("DANGER!!")
    
    frame_counter = 0

    logger.info("Extracting Frames...")
    logger.info(f"[{global_frame_counter} - {global_frame_counter + (num_frame - 33) -1}].jpg")
    while True:
        ret, frame = video.read()
        if not ret or frame_counter >= (num_frame - 33):
            break 
        
        ecef_from_local = quat2rot(frame_orientations[frame_counter])
        local_from_ecef = ecef_from_local.T
        frame_positions_local = np.einsum('ij,kj->ki', local_from_ecef, frame_positions - frame_positions[frame_counter])
        
        # Saving File
        cv2.imwrite(f"{img_dir}/{global_frame_counter}.jpg", frame)
        np.save(f"{pose_dir}/{global_frame_counter}.npy", frame_positions_local[frame_counter:frame_counter+33])

        # Counter Update    
        frame_counter += 1
        global_frame_counter += 1
    logger.info(f"{video_file} Processing Complete!")
 
logger.info("OPERATION COMPLETED!")