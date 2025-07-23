## GUI_Code
from flet import (Column, FloatingActionButton, IconButton, Page, Row, Text, TextField, 
                  Colors, Container, TextThemeStyle, Icons, border, alignment, app)
import sqlite3 

db = sqlite3.connect("phonebook.db", check_same_thread=False)
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS phonebook(name VARCHAR, number VARCHAR)")


class Contact(Container):
    def __init__(self, contact_name, contact_number, contact_delete, contact_update):
        super().__init__()

        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_delete = contact_delete
        self.contact_update = contact_update

        self.display_view_name = Text(value=self.contact_name,
                                      width=200,
                                      style=TextThemeStyle.TITLE_MEDIUM,
                                      text_align=alignment.center)
        self.display_view_number = Text(value=self.contact_number,
                                        width=200,
                                        style=TextThemeStyle.TITLE_MEDIUM,
                                        text_align=alignment.center)
        self.edit_view_name = TextField()
        self.edit_view_number = TextField()
        
        self.display_view = Row(alignment="spaceBetween",
                                vertical_alignment="center",
                                controls=[self.display_view_name,
                                    	self.display_view_number,
                                        Row(spacing=0,
                               			    controls=[
                     					   IconButton(
                     						       icon=Icons.CREATE_OUTLINED,
                      						       tooltip="ویرایش تماس",
                      						       on_click=self.edit_clicked,
                                    ),
                          IconButton(
                              icon=Icons.DELETE_OUTLINE,
                              tooltip="حذف تماس",
                                      on_click=self.delete_clicked,
                        					      ),
                    				          ],
                ),
            ],
        )
        self.edit_view = Row(visible=False,
                             alignment="spaceBetween",
                              vertical_alignment="center",
                              controls=[self.edit_view_name,
                            		    self.edit_view_number,
                                        IconButton(
                                            icon=Icons.DONE_OUTLINE_OUTLINED,
                                            icon_color=Colors.GREEN,
                                            tooltip="ویرایش تماس",
                                            on_click=self.save_clicked,
             					   ),
     				       ], 
        )
        column = Column(controls=[self.display_view, self.edit_view])
        self.content = column
        self.padding = 2
        self.border = border.all(0.2, Colors.BLACK)

    def edit_clicked(self, e):
        self.edit_view_name.value = self.display_view_name.value
        self.edit_view_number.value = self.display_view_number.value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.contact_update(self.display_view_name.value,
                            self.display_view_number.value,
                            self.edit_view_name.value,
                            self.edit_view_number.value)
        self.display_view_name.value = self.edit_view_name.value
        self.display_view_number.value = self.edit_view_number.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.contact_delete(self)


class PhoneBookApp(Container):
    def __init__(self):
        super().__init__()

        self.new_conatact_name = TextField(label="نام")
        self.new_conatact_number = TextField(label="شماره تلفن")
        self.contact_count = 0
        self.contact_count_text = Text(
                			f"{self.contact_count} شماره تلفن موجود است",
                			style=TextThemeStyle.TITLE_SMALL,
color=Colors.RED,
                         	   )
        self.contact_count_text_container = Container(
            					content= self.contact_count_text,
padding= 5
       					      )
        self.contacts = Column()
        self.contacts_container = Container(
                           		       content=self.contacts,
                              padding=5,
                                             bgcolor=Colors.CYAN_100,
                                             width=720
                                           )

        
        self.content = Column(controls=[
               		    Container(
                          		  content= Row(controls=[
    Text(value="دفترچه تلفن",
         style=TextThemeStyle.DISPLAY_SMALL,
  font_family="IranNastaliq")], 
   		      		alignment="center"),
                        		  padding=5,
                        		  bgcolor=Colors.AMBER,
                       		  alignment=alignment.center
                                  ),
               		    Row(controls=[
                				   self.new_conatact_name,
              		   			   self.new_conatact_number,
        			                  FloatingActionButton(
icon=Icons.ADD,    
on_click=self.add_clicked),
                 				   ],
         			        ),
              			    Row(controls=[
                                 		   self.contact_count_text_container,                                
                           			  ],
                           		 alignment="spaceBetween",
                        		 vertical_alignment="center",
                       ),
      			            Column(controls=[
       self.contacts_container
      ],
                   spacing=0,
              				    ),
          		  ],
      		  )

    def load_all_data(self):
        data = cursor.execute("SELECT * FROM phonebook")
        self.contact_count = 0
        for item in data:
            contact = Contact(item[0], item[1],self.contact_delete, self.contact_update)
            self.contacts.controls.append(contact)
            self.contact_count += 1
        self.contact_count_text.value = f"{self.contact_count} شماره تلفن موجود است"
        self.update()

    def did_mount(self):
        self.load_all_data()

    def add_item(self, name, number):
        query = f"INSERT INTO phonebook (name, number) values('{name}', '{number}')"
        cursor.execute(query)
        db.commit()
    
    def edit_item(self, old_name, old_number, new_name, new_number):
        query = f"""
                    UPDATE phonebook SET name='{new_name}', number='{new_number}'
                    WHERE name='{old_name}' AND number='{old_number}'
                 """
        cursor.execute(query)
        db.commit()


    def delete_item(self, name, number):
        query = f"DELETE FROM phonebook WHERE name='{name}' AND number='{number}'"
        cursor.execute(query)
        db.commit()

    def add_clicked(self, e):
        if self.new_conatact_name.value and self.new_conatact_number.value:
            contact = Contact(self.new_conatact_name.value,
                              self.new_conatact_number.value, 
                              self.contact_delete,
                              self.contact_update)
            self.contacts.controls.append(contact)
            self.add_item(self.new_conatact_name.value, self.new_conatact_number.value)
            self.new_conatact_name.value = ""
            self.new_conatact_number.value = ""
            self.new_conatact_name.focus()
            self.contact_count += 1
            self.contact_count_text.value = f"{self.contact_count} شماره تلفن موجود است"
            self.update()

    def contact_update(self, old_name, old_number, new_name, new_number):
        self.edit_item(old_name, old_number, new_name, new_number)

    def contact_delete(self, contact):
        self.contacts.controls.remove(contact)
        self.delete_item(contact.contact_name, contact.contact_number)
        self.contact_count -= 1
        self.contact_count_text.value = f"{self.contact_count} شماره تلفن موجود است"
        self.update()

    def update(self):
        for contact in self.contacts.controls:
            contact.visible = True
        super().update()


def main(page: Page):
    page.title = "دفترچه تلفن"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.window.width = 720
    page.window.center()
    page.rtl = True
    page.window.resizable = False
    page.window.maximizable = False
    page.fonts = {
        "Nastaliq":"fonts/IranNastaliq.ttf"
    }
    page.update()

    phonebook = PhoneBookApp()
    
    page.add(phonebook)


app(target=main)

