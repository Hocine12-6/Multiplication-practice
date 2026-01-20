import random
import os 
import  time 
import  sys 
import platform
   
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[1;94m'
    BLUE_DIM="\033[2;34m"
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    INVERT="\033[7m"
    GOLD="\033[33m"
    ASHEN="\033[90m"  
    
usage_guid=[
     "-Do not insert a comma (it will be considered an introductory phrase).",
     "-Answer with the correct number for the operation.",
     "-Do not enter a negative sign, this is a multiplication learning program.", 
]   

additions= {
    "info": "To display input correction instructions",
    "exit": "To exit the program also you can use 'q'",
    "clear": "To clear the screen",
    "help": "To display the multiplication help list",
    "limits": "To change the random selection limits for x and y",
    "lslimits": "To display the current limits for x and y",
}
advenced_additions=["q",]

external_additions={
   "-limits": "To change the random selection limits for x and y",
}
using_external_additions={
   "-limits":"python program.py -limits [start_x] [end_x] [start_y] [end_y]",
}
encouragement_list = ["Great job!", "You're a legend!", "Outstanding!"]
external_input= sys.argv[1:]#مدخلات خارجية 
max_limitforall = 50
_for_smartRepitition={
                                   "success_counter":0 ,
                                   'errors_for_ripitition':[  ]
}
LSOIO= 5 #Limit_storage_of_incorrect_operations 
def clear_screen():
   """خاصية تنظيف الشاشة مدعومة في كل من أجهزة ميكروسوفت والأنظمة المعتمدة على نواة لينكس."""
   os.system("cls" if os.name == "nt" else "clear")
   #clear_screen= lambda : os.system("cls" if os.name == "nt" else "clear")

def draw_divider_line(color,size,type,stay_on_line):
   """تستخدم لعرض الأسطر """
   def for_line_shape(type):
       if type =="normal":
           return "_"
       elif type=="equal":
           return "="
       else:
           return  "-"
           
   try :
      columns=os.get_terminal_size()[0]
   except:
      columns=79
      
   colors={"blue":Color.BLUE,
                   "gold":Color.GOLD,
                   "cyan":Color.CYAN,
                   "ashen":Color.ASHEN,
                   "fact":Color.END,
                   }
                   
   line_shape = for_line_shape(type)
   
   selected_colors=colors[color]
   real_size=round(columns*(size/100))
   
   the_line=f"{Color.END}{selected_colors}{line_shape*real_size}{Color.END}"
   print(the_line,end="") if stay_on_line else print(the_line)
   
def show_limits(start_x,start_y,limit_x,limit_y):
   """تقوم بعرض الحدود بطريقة جميلة و منسقة """
   draw_divider_line("gold",50,"",False)
   print("X x Y = XY")
   draw_divider_line("fact",15,"",True)
   print("Limits",end="")
   draw_divider_line("fact",15,"",False)
   print(f"X: {start_x} →{limit_x}")
   print(f"          Enter {Color.BLUE}'limits'{Color.END} for change limits")
   print(f"Y: {start_y} →{limit_y}")
   draw_divider_line("gold",50,"",False)
   
def show_usage_guide():
   """عرض تعليمات الإستعمال """
   print(f"{Color.BLUE + Color.INVERT}Program Usage Instructions:",end="")
   print(Color.END+Color.UNDERLINE)
   for instruction in usage_guid:
      print(instruction)
   print(Color.END)
   
def show_additions():
   """عرض الإظافات العادية"""
   print(f"{Color.BLUE + Color.INVERT} Add-ons:{Color.END}",end="")
   print(Color.UNDERLINE)
   for addition in additions:        
        print("Input " + addition, additions[addition])
   print(Color.END)
   
def show_external_additions():
   """عرض الإضافات الخارجية"""
   print(f"{Color.BLUE + Color.INVERT}Command Line Interface Options :",end="")
   print(Color.END)
   for external_addition in external_additions.keys() :
      addition=external_additions[external_addition]
      using=using_external_additions[external_addition]
      
      print(f"{Color.UNDERLINE+Color.GREEN+external_addition+Color.END+Color.UNDERLINE} {addition+Color.END}:")
      print(f"  {using}")
   print()#ليتوافق تركه لمسافة مع باقي دال عرض المعلومات المساعدة
   
def show_input_error(answer):#مدخل خاطئ
            """عرض رسالة خطأ """
            print(f"{Color.RED}The input '{answer}'' incorrect .")
            if "." in answer:
               print("Note: Do not enter numbers containing a comma. ")
            print(f"Please use 'info' to show options {Color.END}")

def show_help_table(min_limit,max_limit):
     """عرض قائمة ضرب محددة"""
     clear_screen()
     max_limit+=1
     number_for_help = input("-Enter a number :")
     
     
     if number_for_help.isdigit():
         number_for_help= int(number_for_help)
         if number_for_help > max_limitforall :
             number_for_help= max_limitforall
             print(Color.GOLD+Color.INVERT+f"Your input over {max_limitforall}, The  number has been equal  {max_limitforall}."+Color.END)
             draw_divider_line("fact",50,"",False)
             
         elif number_for_help == 0 :
             print(Color.GOLD+Color.INVERT+"The all  answes equal 0 "+Color.END)
   
             
         elif number_for_help==1:
             print(Color.GOLD+Color.INVERT+"Man, everything multiplied by one equals itself.")
             print()
             random_number =random.randint(2,max_limitforall)
             print(f" Example :{Color.END} {Color.PURPLE+Color.INVERT}{random_number} x 1 = {random_number} "+Color.END)
        
         else:      
            print(Color.CYAN)
            for r in range(min_limit,max_limit):
                print(f" {number_for_help} x {r} = {number_for_help*r }")
            print(Color.END)
         
     else:
        if number_for_help == "":
            number_for_help= "not_thing"
        print(f"{Color.RED}input error \n<<{number_for_help}>> is not a number{Color.END}")
            
def update_limits(target_str,  now_limit_start,  now_limit_end,  is_external):
   """تستعمل لتغيير الأرقام العشوائية التي ستختار"""
   correct_inputs=True#لتجنب عرض خاطئ في حالة تعيين القيم الإفتراضية
   limits={"new_limit_start":now_limit_start,
      "new_limit_end":now_limit_end
      }
      
   if is_external :
      try:
          for_update_external= external_input[1:3] if target_str=="x" else external_input[3:5]
          new_limit_start,  new_limit_end  =   for_update_external
       
          limits["new_limit_start"]=int(new_limit_start)
          limits["new_limit_end"]=int(new_limit_end)
          
      except:#إذا حدث خطأ نضع قيم إفتراضية مباشرة 
         correct_inputs=False
         limits["new_limit_start"]=2
         limits["new_limit_end"]=10           
         
         
   else:   
      print("--The limits are the values the user might see in this operation--")
      print("--WARNING:All inputs that are zero or one will become 2")
      print("---Do not enter values over 50")
      draw_divider_line("blue",100,"normal",False)
      print(f"{now_limit_start}→..→ {now_limit_end}")
      print("Æ1→..→ Æ2")
      draw_divider_line("fact",20,"",False)
      print("Æ x Y = ÆY " if target_str=="x" else "X x Æ  = XÆ")
      draw_divider_line("fact",20,"noral",False)
   
      for limit in limits.keys():#خاصة بطلب  تعديل القيم و التأكد من صحتها
           while True :
                 new_limit = input(f"Please enter the new limit to replace {limits[limit]}: ")
                 if not new_limit.isdigit():
                    print(f"{Color.RED} It looks like your input is incorrect {Color.END}")
                    continue
                 else:
                    new_limit=int(new_limit)
                    if new_limit < 2:
                       new_limit=2
                    limits[limit]=new_limit
                 break
    
   new_limit_start=limits["new_limit_start"]#للوضوح حددت في متغير واحد 
   new_limit_end=limits["new_limit_end"]
   
   draw_divider_line("blue",90,"",True)#بقاء في السطر لعدم طباعة تغيير اللون 
   
   print(Color.GOLD+Color.INVERT)
   #معالجة user cases
   #WARNING: While modifying the input conditions, please consider the flow of the conditions
   if new_limit_start >max_limitforall or new_limit_end > max_limitforall:#حالات تجاوز الحدود 
       print(f"WARNING :an input has exceeded the limit of 50 ")
       print()
       if new_limit_start>max_limitforall and new_limit_end > max_limitforall:
           new_limit_start, new_limit_end=max_limitforall-1, max_limitforall
           print(f"Limits exceeded 50: The limit has been set to 49→{max_limitforall} ")
           
       elif new_limit_start > max_limitforall:#البداية تجاوز قيمة اقصى حد
           new_limit_start=new_limit_end-1 if new_limit_start==new_limit_end else new_limit_end-1
           print(f"Start limit set to {new_limit_start}")
           
       else:#النهاية تجاوزت 50
           if new_limit_start <50 :
               new_limit_end=max_limitforall
           else:#البداية تساوي 50 و لا تكون أكبر لأنها تعالج في البداية لتصبح 50
                new_limit_end = max_limitforall
                new_limit_start= new_limit_end-1 
                print(f"First value set to {new_limit_start}\n")
 
           print(f"End limit set to {new_limit_end}")
           
   elif  new_limit_start ==new_limit_end:#بداية = نهاية 
      if new_limit_end+1 <=  max_limitforall:
          new_limit_end+=1
          print(f"{Color.GOLD+Color.INVERT}Start and end values are equal; the last value has been set to {new_limit_end}")
      else :
          new_limit_start -= 1
          print(f"{Color.GOLD+Color.INVERT}Start and end values are equal; the first value has been set to {new_limit_start}")
          
      draw_divider_line("blue",90,"",False)
      
   elif new_limit_end<new_limit_start:#بداية أكبر من نهاية 
      new_limit_start,new_limit_end=new_limit_end,new_limit_start
      print("Start values are greater than end values")
      print()
      print("Start and end points have been changed")
      draw_divider_line("blue",90,"",False)
      
   elif correct_inputs:#مدخلات صحيحة
      print("Correct inputs,The borders have been modified")
      draw_divider_line("blue",90,"",False)
   else:#مدخلات خاطئة (تحدث في حالة مدخل خارجي )
      print(f"{Color.RED}An error occurred in the border change input; please correct it manually")
      print()
      print(f"---Default values have been set---.")
      draw_divider_line("blue",90,"",False)
      
   print(Color.END)
   if not is_external :
         input("Press Enter to continue...")
         clear_screen()
   
   return  new_limit_start,new_limit_end
     
def exiting_animation():
    """انيميشن الخروج من البرنامج"""
    clear_screen()
    print(f"{Color.GREEN}Please, if you can, open a PR and update it...")
    time.sleep(2)
    print(f"{Color.RED}Thanks for using this program...{Color.END}")
    time.sleep(2)
    print("Good day, see you later Maestro...")
    time.sleep(2)

def smart_repitition():#new_error == [  x  ,   y  ]   –>True / new_error==False –>False
       otput = []
       the_error=_for_smartRepitition["errors_for_ripitition"][0]
       otput=the_error# the_error–>list 
       _for_smartRepitition['success_counter']=0#تصفير عداد النجاحات
       _for_smartRepitition["errors_for_ripitition"].remove(the_error)#حذف الخطأ المستهدف  
       return  otput

#======tools_tap=====

def show_tools_info():#عرض خيارات الأدوات
    clear_screen()
    draw_divider_line("gold",80,"equal",False)
    for tool in tools_info.keys():
        print(Color.GREEN+f" {tool+Color.END} :{Color.UNDERLINE+tools_info[tool]+Color.END}.")
    draw_divider_line("gold",80,"equal",False)
    input("Press Enter to continue...")
    clear_screen()

def device_info():
      clear_screen()
      system_info = platform.uname()
      print(f"{'Device_name'.ljust(15)}: {system_info.node}")
      print(f"{'OS'.ljust(15)}: {system_info.system} {system_info.release}")
      print(f"{'Processor'.ljust(15)}: {system_info.processor}")
      draw_divider_line("ashen",50,"normal",False)
      input("Press Enter to continue...")
      clear_screen()
      
#____for stsrt the tools
tools_start={#"name_of_tool" : name_of_function
            "dvinfo":device_info
}
hidden_addition=["tools info",]
tools_info={
                    "dvinfo":"Display general device information",
}

#====================
list_of_additions= list(additions.keys())+ advenced_additions+  list(tools_info.keys())+    hidden_addition

def main():
    """البرنامج الأساسي"""
    clear_screen()
    start_x, start_y, limit_x, limit_y = 2, 2 ,10, 10
    
    if external_input:
       if external_input[0] == "-limits":
           clear_screen()
           print("For x limits:")
           for_change_x=update_limits("x",start_x,limit_x,True)
           print("For y  limits:")
           for_change_y=update_limits("y",start_y,limit_y,True)
           start_x,limit_x  =  for_change_x
           start_y,limit_y  =  for_change_y
           
       #elif an other external addition ..... 
       
       
    draw_divider_line("ashen",99,"equal",False)
    print(f"{Color.BLUE+Color.INVERT}Nice to meet you maestro{Color.END}")
    show_limits(start_x,start_y,limit_x,limit_y)
    while True:
        #_____ما يخص العملية 
        y_number = random.randint(start_x, limit_x)
        x_number = random.randint(start_y, limit_y)
        if ( _for_smartRepitition["success_counter"]== 3 
         and len(_for_smartRepitition["errors_for_ripitition"])>=1 ):
            x_number,y_number = smart_repitition()
        operation_parties = [ x_number, y_number ] #[x , y ]–>list
        reight_answer =  operation_parties[0] * operation_parties[1]#تعيين القيمة الصحيحة 
        #__________________
        draw_divider_line("ashen",50,"normal",False)
        print(f"{operation_parties[0]} x {operation_parties[1]}", end="")
        start_time = time.time()
        answer = input(" = ").strip()
        end_time = time.time()
        result_time = round(end_time - start_time, 2)

        if (not answer.isdigit()) and (answer not in list_of_additions): #حالة مدخل خاطئ 
           if answer=="":
              answer="not thing"
           show_input_error(answer)
           
        elif answer == str(reight_answer): #حالة اجابة صحيحة
            _for_smartRepitition['success_counter'] += 1
            print(Color.ASHEN+Color.INVERT+random.choice(encouragement_list)+Color.END)
            print(f"Time taken to answer : {result_time} second")
            if result_time>15:
                print(Color.PURPLE+Color.INVERT+"Don't be sad, even a second of improvement is progress."+Color.END)#استعمال قتموس لرسائل المواسات 

        elif answer in ["exit","q"]: #خروج
            exiting_animation()
            exit()

        elif answer == "info": #مساعدة 
            clear_screen()
            show_usage_guide()
            show_additions()
            show_external_additions()
            draw_divider_line("ashen",50,"normal",False)
            input("Press Enter to back...")
            clear_screen()
            print(f"{Color.CYAN}Please follow the instructions.Thank you... {Color.END}")
 
        elif answer == "tools info":
            show_tools_info()
        elif answer == "clear":#تنظيف شاشة 
            clear_screen()

        elif "help" == answer: #طباعة قائمة ضرب رقم محدد  حتى 10 
             max_limit,min_limit=max(limit_x,limit_y),min(start_x,start_y)
             show_help_table(min_limit,max_limit)

        elif answer == "limits":#تغيير الحدود 
           clear_screen()
           for_change_x=update_limits("x",start_x   , limit_x,False)
           for_change_y=update_limits("y",start_y  ,  limit_y,False)

           _for_smartRepitition["errors_for_ripitition"]=[]
           start_x,limit_x  =  for_change_x#his otput : (start , limit)
           start_y,limit_y  =  for_change_y
 
           clear_screen()
           print(f"{Color.GREEN+Color.UNDERLINE+Color.INVERT}The limits were updated successfully{Color.END}")
           show_limits(start_x,start_y,limit_x,limit_y)
           

        elif answer =="lslimits":#عرض الحدود 
           show_limits(start_x,start_y,limit_x,limit_y)

        elif answer in  tools_info.keys() :
            tools_start[answer]()

            #بعد إظافة الأدات أظف الدالة بدون اقواس للdict  الذي اسمه tools و لا تنسى وضع الكلمة المفتاحية في list_of_tools
        else:#حالة إجابة خاطئة 
            
            _for_smartRepitition['success_counter']=0
            if (len(_for_smartRepitition["errors_for_ripitition"]) <= LSOIO 
              and (
              operation_parties not in _for_smartRepitition["errors_for_ripitition"] 
              or  operation_parties[::-1] not in _for_smartRepitition["errors_for_ripitition"]) 
              ): 
                _for_smartRepitition["errors_for_ripitition"].append(operation_parties)
                
            correct_operation = f' {operation_parties[0]} x {operation_parties[1]} = {reight_answer} '
            print("Wrong...")
            print(f"     <<{Color.GREEN+Color.INVERT}{correct_operation}{Color.END}>>")
 
try:
        main()
except KeyboardInterrupt:
        print(f"\n{Color.RED}Caught you! Trying to escape with Ctrl+C?{Color.END}")
        time.sleep(7)
        exiting_animation()
        exit()
 
 