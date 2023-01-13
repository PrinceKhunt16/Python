import os 

if(os.path.exists('OsModule/Dummy')):
  os.rename('OsModule/Dummy', 'OsModule/Dump')