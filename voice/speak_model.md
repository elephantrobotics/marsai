#*speak_model*
######speak_model 使用pocketsphinx + PyAudio实现其功能
######在该文件中主要有三个主要函数：

`main(speak_queue)`&nbsp;&nbsp;&nbsp;&nbsp;:   
&nbsp;&nbsp;&nbsp;&nbsp; 主函数，其他类调用的接口函数  
&nbsp;&nbsp;&nbsp;&nbsp; speak_queue为存储语音的队列，其最大长度只有1，  
&nbsp;&nbsp;&nbsp;&nbsp; 保证queue存储的随时都是最新的命令

 `speak_monitor()`&nbsp;&nbsp;&nbsp;&nbsp;:  
 &nbsp;&nbsp;&nbsp;&nbsp; 主要代码结构，实现不断接收语音，识别的功能  
 &nbsp;&nbsp;&nbsp;&nbsp; 并将返回结果（返回结果是一个字典类型 {‘type': 1 or 2, ‘word': command, ‘db: db} ）  
 &nbsp;&nbsp;&nbsp;&nbsp; 存入speak_queue中，  
 &nbsp;&nbsp;&nbsp;&nbsp; 存储时会判断speak_queue是否为空，
 若不为空，说明没有被调用，将该命令覆盖掉
 
 `load_file()`&nbsp;&nbsp;&nbsp;&nbsp;:  
 &nbsp;&nbsp;&nbsp;&nbsp; 加载指令文件，并将指令存为列表存入command中
 
 `speak_config()`&nbsp;&nbsp;&nbsp;&nbsp;:  
 &nbsp;&nbsp;&nbsp;&nbsp; 创建一个默认的模型
