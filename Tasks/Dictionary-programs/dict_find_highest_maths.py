"""
** TASK.1 - FIND HIGHEST MATHS MARKS OF A PERSON
marks = {'rama' : {'cs': 45, 'maths' : 70},
         'sita' : {'cs': 50, 'maths' : 64},
         'john' : {'cs':40, 'maths' : 50}
        }
"""
marks = {'rama' : {'cs': 45, 'maths' : 70},
         'sita' : {'cs': 50, 'maths' : 64},
         'john' : {'cs':40, 'maths' : 50}
        }
rama_marks = marks.get('rama').get('maths')
sita_marks = marks.get('sita').get('maths')
john_marks = marks.get('john').get('maths')
cnt = len(marks)
for i in range(1, cnt+1):
        if marks['rama']['maths'] > marks['sita']['maths'] and marks['rama']['maths'] > marks['john']['maths']:
            print('Rama has highest maths marks '+ str(rama_marks))
            break
        elif marks['sita']['maths'] > marks['rama']['maths'] and marks['sita']['maths'] > marks['john']['maths']:
            print('Sita has highest maths marks '+ str(sita_marks))
            break
        elif marks['john']['maths'] > marks['rama']['maths'] and marks['john']['maths'] > marks['sita']['maths']:
            print('John has highest maths marks '+ str(john_marks))
            break