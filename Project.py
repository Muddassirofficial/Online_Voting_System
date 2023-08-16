import flet as ft
from flet import (
   AppBar,Page,Text,colors,ResponsiveRow,Column,Container,Image,Row,alignment,TextField
   ,Border,View,ElevatedButton,margin,CrossAxisAlignment,MainAxisAlignment,padding
)
list = []
vote = []

def block(u_b_cnic,page,error):
   list.remove(u_b_cnic.value)
   print(list)
   u_b_cnic.value = "13101"
   print("added")
   error.value = "User Blocked Successfully !"
   error.visible = True 
   page.update()
 
def click(u_cnic,page,error):
   
   list.append(u_cnic.value)
   print(list)
   u_cnic.value = "13101"
   print("added")
   error.value = "User Added Successfully !"
   error.visible = True 
   page.update()
   

def Rlogin(v_cnic,page,error,welcome):
       
    if v_cnic.value == "" :
        error.value = "Enter CNIC_No"
        error.visible=True 
        print(error)
    elif v_cnic.value in list:
        welcome.value = "CNIC No #" + v_cnic.value
        v_cnic.value = "13101" 
        error.visible=False 
      
        page.go('/next1')
    else:
        error.value = "Please Enter Correct Details"
        error.visible=True
        v_cnic.value = "13101" 
    page.update()


def login(l_cnic, l_pass, page,error):
    if l_cnic.value == "" or l_pass.value == "":
        error.value = "Both TextFields Must Be Filled"
        error.visible=True 
    elif l_cnic.value == "1310199999999" and l_pass.value == "admin123":
        l_cnic.value = "13101" 
        l_pass.value = ""
        error.visible=False    
        page.go('/next')
    else:
        error.value = "Please Enter Correct Details"
        error.visible=True
        l_cnic.value = "13101" 
        l_pass.value = ""
    page.update()  
      
def dropdown_changed(selected, ss,page,ppp,pti,pmln,mqm,jui,error,castebtn,welcome):
        selected.value = ss.value
        if selected.value == "PTI":
           pti.value = str(int(pti.value) + 1)
           error.value = "Vote Casted Successfully !"
           error.visible = True
        elif selected.value == "JUI":
           jui.value = str(int(jui.value) + 1)  
           error.value = "Vote Casted Successfully !"
           error.visible = True
        elif selected.value == "PPP":
           ppp.value = str(int(ppp.value) + 1)
           error.value = "Vote Casted Successfully !"
           error.visible = True
        elif selected.value == "MQM":
           mqm.value = str(int(mqm.value) + 1)
           error.value = "Vote Casted Successfully !"
           error.visible = True 
        elif selected.value == "PMLN":
           pmln.value = str(int(pmln.value) + 1)
           error.value = "Vote Casted Successfully !"
           error.visible = True 
        else:
           error.visible = True
        vote.append(welcome.value)
        print(vote)   
        castebtn.disabled = True
        ss.disabled=True     
        page.update()


def main(page: ft.Page):
 page.title = "Voting System"
 page.window_width = 390 
 page.window_height = 844
 page.horizontal_alignment = 'center'
 page.vertical_alignment = 'center'
 

 #selection
 ss = ft.Dropdown(label = "Select Party",
                width=200,
               
                options=[
                ft.dropdown.Option("PTI"),
                ft.dropdown.Option("JUI"),
                ft.dropdown.Option("PPP"),
                ft.dropdown.Option("MQM"),
                ft.dropdown.Option("PMLN"),
                
        ],
        #on_change=lambda e: dropdown_changed(selected, ss,page,ppp),
    ) 
 castebtn = ft.ElevatedButton(text='Caste Vote Now',bgcolor='#b48811',on_click=lambda e: dropdown_changed(selected,ss,page,ppp,pti,pmln,mqm,jui,error,castebtn,welcome))  
 selected =  ft.TextField(label="You Choosed",border_color='#b48811',disabled=True,width=450)
 pti =  ft.TextField(label="PTI Total Votes",value="0", width=350,disabled=True,text_align='center',text_size=25)
 jui =  ft.TextField(label="JUI Total Votes",value="0", width=350,disabled=True,text_align='center',text_size=25)
 ppp =  ft.TextField(label="PPP Total Votes",value="0", width=350,disabled=True,text_align='center',text_size=25)
 mqm =  ft.TextField(label="MQM Total Votes",value="0", width=350,disabled=True,text_align='center',text_size=25)
 pmln = ft.TextField(label="PMLN Total Votes",value="0", width=350,disabled=True,text_align='center',text_size=25)
 error = ft.Text(value="Something went wrong ! Try Again Later",visible=False)
 div = ft.Divider(height=39, thickness=4)
 #routing
 btn = ElevatedButton(text='Next Page', on_click=lambda _: page.go('/'))
 #reset = ft.ElevatedButton(text="Reset System",bgcolor='#b48811',on_click=lambda _: (setattr(ss, "disabled", False),setattr(error, "visible", False),setattr(castebtn, "disabled", False)))

 #Admin_login
 l_txt = ft.Text(value="LogIn Now",size=20)
 l_cnic = ft.TextField(label="CNIC No",border_color='#b48811',max_length=13,value=13101,width=450)
 l_pass = ft.TextField(label="Password", password=True, can_reveal_password=True,border_color='#b48811',width=450,max_length=13)
 #l_btn = ft.ElevatedButton(text="LogIn",bgcolor='#b48811',on_click=lambda _: page.go('/next'))
 l_btn = ft.ElevatedButton(text="LogIn",bgcolor='#b48811',on_click=lambda _: login(l_cnic, l_pass, page,error))

 #Voter_login
 v_txt = ft.Text(value="LogIn Now",size=20)
 v_cnic = ft.TextField(label="CNIC No",border_color='#b48811',max_length=13,value=13101,width=450)
 #v_btn = ft.ElevatedButton(text="LogIn",bgcolor='#b48811',on_click=lambda _: page.go('/next1'))
 v_btn = ft.ElevatedButton(text="LogIn",bgcolor='#b48811',on_click=lambda _: Rlogin(v_cnic,page,error,welcome))
 #welcome
 welcome = ft.Text(value="Welcome",size=20)



 #Add User
 u_txt = ft.Text(value="Add New User",size=20)
 u_b_txt = ft.Text(value="Block User",size=20)
 u_name = ft.TextField(label="Full Name",border_color='#b48811',width=450)
 u_cnic = ft.TextField(label="CNIC No",border_color='#b48811',max_length=13,value=13101,width=450)
 u_b_cnic = ft.TextField(label="CNIC No",border_color='#b48811',max_length=13,value=13101,width=450)
 u_btn = ft.ElevatedButton(text="Upload Record",bgcolor='#b48811',on_click=lambda _: click(u_cnic,page,error))
 u_del_btn = ft.ElevatedButton(text="Block User",bgcolor='#b48811',on_click=lambda _: block(u_b_cnic,page,error))
 def route_change(route):
  if page.route == '/':
   page.views.clear()
   
   error.visible=False
   page.views.append(    
   View (
   route='/',
   controls=[
   ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Voter Pannel ",
                icon = ft.icons.PERSON_PIN,
                content=ft.Column(
                [  
                div,
                v_txt,
                v_cnic,
                v_btn,
                error,
                ft.Text(value="Developed By Muddassir Farooq",size=14,color='#b48811'),
                
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                
                ),
                
            ),
            ft.Tab(
                text="Admin Pannel ",
                icon=ft.icons.PERSON_2_ROUNDED,
                content=ft.Column(
                [  
                div,
                l_txt,
                l_cnic,
                l_pass,
                l_btn,
                error,
                ft.Text(value="Developed By Muddassir Farooq",size=14,color='#b48811'),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER               
                )
            ),
            ft.Tab(
                #text="About Us ",
                icon=ft.icons.APP_REGISTRATION,
                content=ft.Column(
                [
                ft.Divider(height=39, thickness=4), 
                ft.Text(value="About Us",size=30),
                ft.Text(value="This Ia A UI BASES WEB APPLICATION DESIGNED IN PYTHON \n\nWe'd love to hear your feedback, suggestions, or any questions you may have. Feel free to reach out to us at msmtimes21@gmail.com  \n\n> COPYRIGHT @ MUDDASSIR FAROOQ",text_align='justify'),
                ],
                )
             
            ),
            
        ],
        expand=1,
        unselected_label_color='GREY'
    )
   
   ],
   appbar = AppBar(title=Text("Vote Casting System"),center_title=True,bgcolor='#b48811',color='#b48811'),
   padding=30,
   
   )
  
  )



   
  elif page.route == '/next':
    error.visible=False

    page.views.append(
    View (
    route='/next',
    controls=[
    ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Add New User ",
                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                content=ft.Column(
                [  
                div,
                u_txt,
                u_cnic,
                u_btn,
                error,
                ft.Text(value="Developed By Muddassir Farooq",size=14,color='#b48811'), 
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER               
                )
            ),
            ft.Tab(
                text="Block User ",
                icon=ft.icons.BLOCK_OUTLINED,
                content=ft.Column(
                [  
                div,
                u_b_txt,
                u_b_cnic,
                u_del_btn,
                error,
                ft.Text(value="Developed By Muddassir Farooq",size=14,color='#b48811'), 
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER               
                )
            ),
            ft.Tab(
                text="Total Votes Caste ",
                icon=ft.icons.SEARCH,
                content=ft.Column(
                [ 
                div,
                ft.Text(value="Casted Votes",size=28),    
                div,   
                pti,
                jui,
                ppp,
                mqm,
                pmln,
                ft.Text(value="Developed By Muddassir Farooq",size=14,color='#b48811'),
                
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER               
                )
            ),
        ],
        expand=1,
    )
   
    ],
    
    appbar = AppBar(title=Text("Admin Pannel"),center_title=True,bgcolor='#b48811'),
    padding=30,
    )
  )
    
  elif page.route == '/next1':
    
    if welcome.value in vote:
           castebtn.disabled = True
           ss.value="Already Vote Casted"
           selected.value="Already Vote Casted"
           ss.disabled=True
           print("Cant Vote")
    else:
           selected.value=""
           castebtn.disabled = False
           ss.disabled=False 
    error.visible=False
               
    page.views.append(
    View (
    route='/next1',
    controls=[
    ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Caste Your Vote ",
                icon=ft.icons.NOTE_ADD,
                content=ft.Column(
                [ 
                div,
                welcome,
                ss,
                selected,
                castebtn,
                error,
                ft.Text(value="Developed By Muddassir Farooq",size=14,color='#b48811'),   
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER               
                )
            ),
        ],
        expand=1,
    )
   
    ],
    appbar = AppBar(title=Text("Voter Pannel"),center_title=True,bgcolor='#b48811'),
    padding=30,
    )
  )

    page.update()
 
 def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
 
 page.on_route_change = route_change
 page.on_view_pop = view_pop
 page.go(page.route)
 
ft.app(target=main)
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)

