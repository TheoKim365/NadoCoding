import os

# print(os.getcwd())  # 현재 작업 디렉토리 
# os.chdir('rpa_basic')
# print(os.getcwd())
# os.chdir('..')  # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir('../..')  # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir('c:/')  # 부모 폴더로 이동
# print(os.getcwd())


## 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), 'my-file.txt')  # 절대경로 생성 
# print(file_path)


## 파일 경로에서 폴더 정보 가져오기 
# print(os.path.dirname(r'C:\Users\wizue\PythonWorks\NadoCoding\my_file.txt'))


# ## 파일 정보 가져오기
# import time
# import datetime

# from cv2 import FileNode_NAMED


# ## 파일의 생성 날짜 (ctime)
# file_path = 'rpa_basic/2_desktop/11_file_system.py'

# ctime = os.path.getctime(file_path)
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime))
# # 날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d %H:%M:%S'))
# print(datetime.datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S'))


# ## 파일의 수정 날짜 (mtime)
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S'))


# ## 파일의 마지막 접근 날짜 (atime)
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime('%Y-%m-%d %H:%M:%S'))


# ## 파일 크기
# fsize = os.path.getsize(file_path)
# print(fsize)   # 파일 크기를 바이트 단위로 가져옴 


## 파일 목록 가져오기
# print(os.listdir())  # 모든 폴더, 파일 목록 가져오기 
# print(os.listdir('rpa_basic'))  # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기 


## 파일 목록 가져오기 (하위폴더 포함)
# result = os.walk('rpa_basic')   # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기 
# # result = os.walk('.')   # 현재 폴더 밑에서 모든 폴더, 파일 목록 가져오기 (숨긴 항목도 가져옴)
# # print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)


# ## 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = '11_file_system.py'
# result = []
# for root, dirs, files in os.walk('.'):
# # for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)


# ## 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# # *.xlsx,, *.txt, 자동화*.png 
# import fnmatch
# pattern = 'file*.png'
# result =[]
# for root, dirs, files in os.walk('.'):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)


# ## 주어진 경로가 파일인지 폴더인지?
# print(os.path.isdir('rpa_basic'))  # rpa_basic은 폴더인지? True 
# print(os.path.isfile('rpa_basic'))  # rpa_basic은 폴더인지? False 

# print(os.path.isdir('run_btn.png'))  
# print(os.path.isfile('run_btn.png')) 

# # 만약에 지정된 경로가 해당하는 파일/폴더가 없더면? 
# print(os.path.isfile('runn_btn.png'))  


# ## 주어진 경로가 존재하는지?
# if os.path.exists('rpa_basic'):
#     print('파일 또는 폴더가 존재합니다.')
# else:
#     print('존재하지 않습니다.')


## 파일 만들기
# 예전에는 with open('파일명', encoding= ) as f:
#   ... 

# open('new_file.txt', 'a').close()  # 빈 파일 생성

## 파일명 변경하기 
# os.rename('new_file.txt', 'new_file_rename.txt')

## 파일 삭제하기
# os.remove('new_file_rename.txt')

## 폴더 만들기
# os.mkdir('new_folder')
# os.mkdir(r'C:\Users\wizue\PythonWorks\NadoCoding\test')  # 절대경로 기준으로 폴더 생성 

# os.mkdir('new_folders/a/b/c')  # 하위 폴더를 가지는 폴더 생성 시도 => 실패
# os.makedirs('new_folders/a/b/c')  # 하위 폴더를 가지는 폴더 생성 시도 => 성공

## 폴더명 변경하기
# os.rename('new_folder','new_folder_rename')


## 폴더 지우기
# os.rmdir('new_folder_rename')
# os.rmdir('new_folders')  # 실패 => 폴더가 비어 있을 때만 가능 

##=========================================================================================
import shutil
# shutil.rmtree('new_folders')  # 폴더 안이 비어 있지 않아도 완전 삭제 가능  !!! 주의 필요 !!!

## 파일 복사하기 
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy('run_btn.png', 'test_folder') # 원본 경로, 대상 경로  => 오류: 폴더 없으면 대상파일을 생성
# print(os.path.exists('test_folder'))
# shutil.copy('run_btn.png','test_folder/copied_run_btn.png')  # 원본 경로, 대상 경로의 새로운 파일이름으로 복사

# shutil.copyfile('run_btn.png','test_folder/copied_run_btn_2.png') # 원본 파일 경로, 대상 파일 경로/파일명

# shutil.copy('run_btn.png','test_folder/copy.png') 
# shutil.copy2('run_btn.png','test_folder/copy_2.png') 

# copy copyfile : 메타정보 복사 x 
# copy2         : 메타정보 복사 O 

##=================================
# 폴더 복사
# shutil.copytree('test_folder', 'test_folder2') # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree('test_folder', 'test_folder3') # 원본 폴더 경로, 대상 폴더 경로

## 폴더 이동 
# shutil.move('test_folder','test_folder3')
# shutil.move('test_folder2','test_folder3')
shutil.move('test_folder3','test_folder')      # 폴더명이 없으면, 폴더명이 바뀌는 효과

