import clr
import entropy
clr.AddReference('System.IO')
clr.AddReference('System.Drawing')
clr.AddReference('System.Reflection')
clr.AddReference('System.Threading')
clr.AddReference('System.Windows.Forms')


import System.IO
import System.Drawing
import System.Reflection
import System.Threading
import System.Windows.Forms as winform

# num = entropy.best_num()
# print(num)






class form1(winform.Form):
    def __init__(self):
        super(form1, self).__init__()
        #define a caption 
        self.Text = 'GUESS THE NUMBER'
        #define a color
        self.BackColor = System.Drawing.Color.FromArgb(200,200,200)

        #define the FIRST label
        global q_0 , q_1
        q_0 = self.LibraryLabel = winform.Label()
        q_0.Text = "PICK A NUMBER BETWEEN 1 _ 10, AND I GUESS IT ;)"
        q_0.Font = System.Drawing.Font("Arial (Body CS)", System.Single(14))
        q_0.Location = System.Drawing.Point(10, 100)
        q_0.Size = System.Drawing.Size(self.LibraryLabel.PreferredWidth, self.LibraryLabel.PreferredWidth)

        #define other labels
        global notic
        notic = self.LibraryLabel = winform.Label()
        notic.Text = "Thank you for putting this project into considration. \n \n Credits : Amin Soleimani \n \n Phone Number : +989017533218 \n \n Email Address : Amiin.soleiimanii@gmail.com"
        notic.Font = System.Drawing.Font("Arial (Body CS)", System.Single(14))
        notic.Location = System.Drawing.Point(18, 100)
        notic.Size = System.Drawing.Size(self.LibraryLabel.PreferredWidth, self.LibraryLabel.PreferredWidth)
       

    



        #define the window size
        self.ClientSize = System.Drawing.Size(500,500)

        #define the minimumn size
        cap_height = winform.SystemInformation.CaptionHeight
        self.MinimumSize = System.Drawing.Size(150, (150 + cap_height))

        #define buttons
        global button1 , button2 , start , end , credit
        start = self.LoadFileButton = winform.Button()
        credit = self.LoadFileButton = winform.Button()
        end = self.LoadFileButton = winform.Button()
        button1 = self.LoadFileButton = winform.Button()
        button2 = self.LoadFileButton = winform.Button()
        start.FlatStyle = winform.FlatStyle.Popup
        credit.FlatStyle = winform.FlatStyle.Popup
        end.FlatStyle = winform.FlatStyle.Popup
        button1.FlatStyle = winform.FlatStyle.Popup
        button2.FlatStyle = winform.FlatStyle.Popup
        
        
        #define the size of the button
        start.Size = System.Drawing.Size(150, 70)
        end.Size = System.Drawing.Size(110, 50)
        credit.Size = System.Drawing.Size(110, 50)
        button1.Size = System.Drawing.Size(100, 50)
        button2.Size = System.Drawing.Size(100, 50)

        #define the location of the button
        start.Location = System.Drawing.Point(177, 300) 
        end.Location = System.Drawing.Point(350, 400)
        credit.Location = System.Drawing.Point(50, 400)
        button1.Location = System.Drawing.Point(30, 400) 
        button2.Location = System.Drawing.Point(360, 400) 

        #define the text of
        credit.Text = "CREDITS" 
        end.Text = "OK"
        start.Text = "START"
        button1.Text = "YES"
        button2.Text = "NO"

        # define the color of the button
        start.ForeColor = System.Drawing.Color.FromName('White')
        end.ForeColor = System.Drawing.Color.FromName('White')
        credit.ForeColor = System.Drawing.Color.FromName('White')
        button1.ForeColor = System.Drawing.Color.FromName('White')
        button2.ForeColor = System.Drawing.Color.FromName('White')
        start.BackColor = System.Drawing.Color.FromArgb(255,69,90,100)
        end.BackColor = System.Drawing.Color.FromArgb(255,69,90,100)
        credit.BackColor = System.Drawing.Color.FromArgb(255,69,90,100)
        button1.BackColor = System.Drawing.Color.FromArgb(255,69,90,100)
        button2.BackColor = System.Drawing.Color.FromArgb(255,69,90,100)

        #define the font of the button
        start.Font = System.Drawing.Font("Arial (Body CS)", System.Single(14))
        end.Font = System.Drawing.Font("Arial (Body CS)", System.Single(14))
        credit.Font = System.Drawing.Font("Arial (Body CS)", System.Single(14))
        button1.Font = System.Drawing.Font("Arial (Body CS)", System.Single(14))
        button2.Font = System.Drawing.Font("Arial (Body CS)", System.Single(14))


        #define controls(adds the defined button to the form)
        self.Controls.Add(start)
        self.Controls.Add(q_0)
        

        #Bind EVENTS to our CONTROL
        start.MouseClick += self.start
        end.MouseClick += self.ok
        credit.MouseClick += self.credit
       
        button1.MouseEnter += self.event1
        button2.MouseEnter += self.event2
        button1.MouseLeave += self.event1_1
        button2.MouseLeave += self.event2_1
        button1.MouseClick += self.yes
        button2.MouseClick += self.no
        
    def make_new_q(self):
        global num
        num = entropy.best_num()
        if num == 10:
            q = self.LibraryLabel = winform.Label()
            q.Text = "Is your number, even ?"
            q.Font = System.Drawing.Font("Arial (Body CS)", System.Single(20))
            q.Location = System.Drawing.Point(30, 100)
            q.Size = System.Drawing.Size(self.LibraryLabel.PreferredWidth, self.LibraryLabel.PreferredWidth)     
        else:
            q = self.LibraryLabel = winform.Label()
            q.Text = ("Is it greater than or equal to " + str(num))
            q.Font = System.Drawing.Font("Arial (Body CS)", System.Single(20))
            q.Location = System.Drawing.Point(30, 100)
            q.Size = System.Drawing.Size(self.LibraryLabel.PreferredWidth, self.LibraryLabel.PreferredWidth)
        return q


    def last_label(self):
        global answer
        answer = entropy.give_value()
        q_1 = self.LibraryLabel = winform.Label()
        q_1.Text = ("Your number is " + str(answer) )
        q_1.Font = System.Drawing.Font("Rockwell", System.Single(20))
        q_1.Location = System.Drawing.Point(30, 100)
        q_1.Size = System.Drawing.Size(self.LibraryLabel.PreferredWidth, self.LibraryLabel.PreferredWidth)

        return q_1
         

    '''
    DEFINING EVENTS

    '''    


     #EVENTS WHEN MOUSE ENTER THE BUTTON
    def event1(self, sender, args):
        button1.BackColor = System.Drawing.Color.FromArgb(25,69,90,100)
       

    def event2(self, sender, args):
       button2.BackColor = System.Drawing.Color.FromArgb(25,69,90,100)


    #EVENTS WHEN MOUSE LEAVE THE BUTTON
    def event1_1(self, sender, args):
       button1.BackColor = System.Drawing.Color.FromArgb(255,69,90,100)
       
    def event2_1(self, sender, args):
       button2.BackColor = System.Drawing.Color.FromArgb(255,69,90,100)

    #EVENT WHEN YOU CLICK "START"
    def start(self, sender, args):
        global q
        q = self.make_new_q()
        self.Controls.Add(button1)
        self.Controls.Add(button2)   
        self.Controls.Remove(start)
        self.Controls.Remove(q_0)
        self.Controls.Add(q)


    def yes(self, sender, args): 
        global num, q, q_1
        self.Controls.Remove(q)
        entropy.deleting_num0(num)
        q = self.make_new_q()       
        self.Controls.Add(q)
        if entropy.check() == 1:
            q_1 = self.last_label()
            self.Controls.Remove(q)       
            self.Controls.Add(q_1)
            self.Controls.Remove(button1)
            self.Controls.Remove(button2)
            self.Controls.Add(end)
            self.Controls.Add(credit)
         


    def no(self, sender, args): 
        global num, q, q_1
        self.Controls.Remove(q)
        entropy.deleting_num1(num)
        q = self.make_new_q()        
        self.Controls.Add(q)
        if entropy.check() == 1:
            q_1 = self.last_label()
            self.Controls.Remove(q)       
            self.Controls.Add(q_1)
            self.Controls.Remove(button1)
            self.Controls.Remove(button2)
            self.Controls.Add(end)
            self.Controls.Add(credit)



    def ok(self, sender, args):
        windows_form = winform.Application()
        windows_form.Exit()    


    def credit(self, sender, args): 
        self.Controls.Remove(end)
        self.Controls.Remove(credit)
        self.Controls.Remove(q_1)
        self.Controls.Add(notic)
          

       
'''
RUNNING THE FORM

'''

def main():
    guess_num = form1()

    print("new form created")
    windows_form = winform.Application()
    windows_form.Run(guess_num)




if __name__ == '__main__':
    main()





