import os 
import log21
from pathlib import Path

log21.print(log21.get_color('#FF0000') + 'This' + log21.get_color((0, 255, 0)) + ' is' + log21.get_color('Blue') +
            ' Blue' + log21.get_colors('BackgroundWhite', 'Black') + ' 8)')

logger = log21.get_logger('My Logger', level_names={21: 'SpecialInfo', log21.WARNING: ' ! ', log21.ERROR: '!!!'})

# -hls_time 设置每片的长度，单位为秒
# -hls_list_size n: 保存的分片的数量，设置为0表示保存所有分片
# -hls_segment_filename ：段文件的名称，%05d表示5位数字
def split_video(source_file:str,desc_dir:str,hls_time=10,hls_list_size=0):
    
    if not os.path.exists(source_file):
      logger.error(f"file not found: [{source_file}]")
      return
    
    if not os.path.lexists(desc_dir):
      os.makedirs(desc_dir)

    filename = Path(source_file).stem

    cmd = f'''ffmpeg \
            -i {source_file} \
            -hls_time {hls_time} \
            -hls_list_size {hls_list_size} \
            -hls_segment_filename {os.path.join(desc_dir,filename+"_%05d.ts")} \
            {os.path.join(desc_dir,filename+".m3u8")}'''
    
    logger.debug(cmd)

    os.system(cmd)

def combine_video(filename:str,output_file:str):
    if not os.path.exists(filename):
      logger.error(f"file not found: [{filename}]")
      return

    dirname = os.path.dirname(output_file)
    if not os.path.lexists(dirname):
        os.makedirs(dirname)
    
    os.system(f"ffmpeg -i {filename} {output_file}")
   

# split_video("./video/Wood.mp4","./hls")
combine_video("./hls/Wood.m3u8","./combin_video/test.mp4")