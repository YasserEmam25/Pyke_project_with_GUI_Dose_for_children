import tkinter as tk
import tkinter.font as font

ages_dic = {'1-7 days': 1, '8-28 days': 2}

medicines = ['Amikin', 'Ceftazidime', 'Gentamicin', 'Imipenem and cilastatin', 'Meropenem', 'Vancomycin', 'Fluconazole',
             'Acyclovir', 'Linezolid', 'Clindamycin', 'Colistimethate Sodium', 'Piperacillin', 'Ampicillin',
             'Metronidazole', 'Ciprofloxacin']

medicines_dic = {'Amikin': 1, 'Ceftazidime': 2, 'Gentamicin': 3, 'Imipenem and cilastatin': 4, 'Meropenem': 5,
                 'Vancomycin': 6, 'Fluconazole': 7, 'Acyclovir': 8, 'Linezolid': 9, 'Clindamycin': 10,
                 'Colistimethate Sodium': 11, 'Piperacillin': 12, 'Ampicillin': 13, 'Metronidazole': 14,
                 'Ciprofloxacin': 15}

meningitis_dic = {'Yes': 'y', 'No': 'n'}

thrush_dic = {'Yes': 'y', 'No': 'n'}

preterm_dic = {'Preterm (uterine age < 37 weeks)': 1, 'Term (uterine age > 37 weeks)': 2}


def gui_main_page():
    frame = tk.Tk()
    frame.minsize(800, 1000)
    global_font = font.Font(family='Helvetica', size=30)
    global_font2 = font.Font(family='Helvetica', size=15)

    space1 = tk.Label(frame, text=' ')
    space2 = tk.Label(frame, text=' ')
    space3 = tk.Label(frame, text=' ')
    space4 = tk.Label(frame, text=' ')

    space1.pack()
    space2.pack()

    medicine_label = tk.Label(frame, text='Choose the name of the medicament', font=global_font)
    medicine_label.pack()

    space3.pack()

    medicines_value = tk.StringVar(frame)
    medicines_dropDown = tk.OptionMenu(frame, medicines_value, *medicines)
    medicines_dropDown.pack()

    space4.pack()

    def button_click():
        frame.destroy()
        gui_medicine_form(medicine_num=medicines_dic[medicines_value.get()])

    button = tk.Button(frame, text='Submit', command=button_click,font=global_font2)
    button.pack()

    frame.mainloop()

    return medicines_dic[medicines_value.get()]


def amikin_dose_form(input_file, weight):
    frame = tk.Tk()
    frame.minsize(400, 600)
    global_font = font.Font(family='Helvetica', size=15)
    space1 = tk.Label(frame, text=' ')
    space1.pack()

    label = tk.Label(frame, text='Enter the dose allowed according to postnatal age in days')
    label.pack()

    space2 = tk.Label(frame, text=' ')
    space2.pack()

    dose_entry = tk.Entry(frame)
    dose_entry.pack()

    space3 = tk.Label(frame, text=' ')
    space3.pack()

    def button_clicked():
        frame.destroy()
        input_file.write(str(dose_entry.get()) + '\n')
        input_file.write(str(weight) + '\n')
        # input_file.close()
        return

    button = tk.Button(frame, text='Submit', command=button_clicked,font=global_font)
    button.pack()

    frame.mainloop()


def gui_medicine_form(medicine_num):
    frame = tk.Tk()
    global_font = font.Font(family='Helvetica', size=15)
    frame.minsize(800, 1000)

    space1 = tk.Label(frame, text='')
    space1.pack()

    inputs = []
    inputs_labels = []

    if medicine_num == 1:
        inputs_labels.append('age')
        inputs_labels.append('menin')
        inputs_labels.append('uterine')
        inputs_labels.append('dose')
        inputs_labels.append('weight')
    elif medicine_num == 2:
        inputs_labels.append('age')
        inputs_labels.append('menin')
        inputs_labels.append('weight')
    elif medicine_num == 3:
        inputs_labels.append('age')
        inputs_labels.append('uterine')
        inputs_labels.append('weight')
    elif medicine_num == 4:
        inputs_labels.append('age')
        inputs_labels.append('weight')
    elif medicine_num == 5:
        inputs_labels.append('age')
        inputs_labels.append('menin')
        inputs_labels.append('weight')
        inputs_labels.append('dose')
    elif medicine_num == 6:
        inputs_labels.append('age')
        inputs_labels.append('menin')
        inputs_labels.append('uterine')
        inputs_labels.append('weight')
    elif medicine_num == 7:
        inputs_labels.append('age')
        inputs_labels.append('thrush')
        inputs_labels.append('uterine')
        inputs_labels.append('weight')
    elif medicine_num == 8:
        inputs_labels.append('uterine')
        inputs_labels.append('weight')
    elif medicine_num == 9:
        inputs_labels.append('age')
        inputs_labels.append('uterine')
        inputs_labels.append('weight')
    elif medicine_num == 10:
        inputs_labels.append('age')
        inputs_labels.append('weight')
        inputs_labels.append('dose')
    elif medicine_num == 11:
        inputs_labels.append('weight')
    elif medicine_num == 12:
        inputs_labels.append('age')
        inputs_labels.append('weight')
    elif medicine_num == 13:
        inputs_labels.append('weight')
        inputs_labels.append('preterm')
    elif medicine_num == 14:
        inputs_labels.append('uterine')
        inputs_labels.append('weight')
    elif medicine_num == 15:
        inputs_labels.append('weight')

    for inp in inputs_labels:
        space = tk.Label(frame, text=' ')
        space.pack()

        if inp == 'age':
            ages_label = tk.Label(frame, text='The Age of the baby is between: ',font=global_font)
            ages_label.pack()
            ages = ['1-7 days', '8-28 days']
            ages_value = tk.StringVar(frame)
            ages_dropDown = tk.OptionMenu(frame, ages_value, *ages)
            ages_dropDown.pack()
            inputs.append(ages_value)
        elif inp == 'menin':
            meningitis_label = tk.Label(frame, text='Does the baby has Meningitis? ',font=global_font)
            meningitis_label.pack()
            meningitis = ['Yes', 'No']
            meningitis_value = tk.StringVar(frame)
            meningitis_dropDown = tk.OptionMenu(frame, meningitis_value, *meningitis)
            meningitis_dropDown.pack()
            inputs.append(meningitis_value)
        elif inp == 'weight':
            weight_label = tk.Label(frame, text='The weight of the baby: ',font=global_font)
            weight_label.pack()
            weight_entry = tk.Entry(frame)
            weight_entry.pack()
            inputs.append(weight_entry)
        elif inp == 'uterine':
            label_text = tk.StringVar()
            label_text.set('Enter the uterine age of the baby:')
            uterine_label = tk.Label(frame, textvariable=label_text,font=global_font)
            if medicine_num == 14:
                label_text.set('Enter the uterine age of the baby (should be greater than 24): ')
            elif medicine_num == 9:
                label_text.set('Enter the uterine age of the baby (should be smaller than 36): ')
            elif medicine_num == 7:
                label_text.set('Enter the uterine age of the baby: ')
            uterine_label.pack()
            uterine_entry = tk.Entry(frame)
            uterine_entry.pack()
            inputs.append(uterine_entry)
        elif inp == 'dose':
            dose_label = tk.Label(frame,
                                  text='Enter the dose allowed according to postnatal age in days (leave blank if it is not needed)',font=global_font)
            dose_label.pack()
            dose_entry = tk.Entry(frame)
            dose_entry.pack()
            inputs.append(dose_entry)
        elif inp == 'thrush':
            thrush_label = tk.Label(frame, text='Does the baby has a Thrush? ',font=global_font)
            thrush_label.pack()
            thrush = ['Yes', 'No']
            thrush_value = tk.StringVar(frame)
            thrush_dropDown = tk.OptionMenu(frame, thrush_value, *thrush)
            thrush_dropDown.pack()
            inputs.append(thrush_value)
        elif inp == 'preterm':
            preterm_label = tk.Label(frame, text='Choose the uterine age according to Preterm or Term:',font=global_font)
            preterm_label.pack()
            preterm = ['Preterm (uterine age < 37 weeks)', 'Term (uterine age > 37 weeks)']
            preterm_value = tk.StringVar(frame)
            preterm_dropDown = tk.OptionMenu(frame, preterm_value, *preterm)
            preterm_dropDown.pack()
            inputs.append(preterm_value)

    def button_click():
        inp_file = open("input.txt", "a")

        inp_file.write(str(medicine_num) + '\n')

        uterine = True
        dose = True
        frame_destroyed = False
        for (label, inp) in zip(inputs_labels, inputs):
            if label == 'age':
                inp_file.write(str(ages_dic[inp.get()]) + '\n')
                if medicine_num == 5 and str(ages_dic[inp.get()]) == '1':
                    uterine = False
                elif medicine_num == 1 and str(ages_dic[inp.get()]) == '2':
                    dose = False
            elif label == 'menin':
                inp_file.write(str(meningitis_dic[inp.get()]) + '\n')
                if (medicine_num == 1 or medicine_num == 6) and meningitis_dic[inp.get()] == 'y':
                    uterine = False
                elif medicine_num == 5 and meningitis_dic[inp.get()] == 'y':
                    uterine = False
            elif label == 'weight':
                inp_file.write(str(inp.get()) + '\n')
            elif label == 'uterine' and uterine:
                inp_file.write(str(inp.get()) + '\n')
                if medicine_num == 1 and int(inp.get()) < 30:
                    dose = False
            elif label == 'dose' and dose:
                inp_file.write(str(inp.get()) + '\n')
            elif label == 'thrush':
                inp_file.write(str(thrush_dic[inp.get()]) + '\n')
            elif label == 'preterm':
                inp_file.write(str(preterm_dic[inp.get()]) + '\n')

        inp_file.close()
        if not frame_destroyed:
            frame.destroy()

    space2 = tk.Label(frame, text=' ')

    space2.pack()

    button = tk.Button(frame, text='Submit', command=button_click,font=global_font)
    button.pack()

    frame.mainloop()


def tkinter_gui_out(first, second, third, forth, fifth):
    frame = tk.Tk()
    frame.minsize(800, 1000)
    global_font = font.Font(family='Helvetica', size=15)
    space1 = tk.Label(frame, text=' ')
    space2 = tk.Label(frame, text=' ')
    space3 = tk.Label(frame, text=' ')
    space4 = tk.Label(frame, text=' ')
    space5 = tk.Label(frame, text=' ')
    space6 = tk.Label(frame, text=' ')
    space7 = tk.Label(frame, text=' ')
    space8 = tk.Label(frame, text=' ')
    space9 = tk.Label(frame, text=' ')
    space10 = tk.Label(frame, text=' ')
    space1.pack()
    space2.pack()

    label1 = tk.Label(frame, text=f'Analysis method: {first}',font=global_font)
    label1.pack()

    space5.pack()
    space6.pack()

    label2 = tk.Label(frame, text=f'Solution Type: : {second}',font=global_font)
    label2.pack()

    space7.pack()
    space8.pack()

    label3 = tk.Label(frame, text=f'Solution Type: : {third}',font=global_font)
    label3.pack()

    space9.pack()
    space10.pack()

    label4 = tk.Label(frame, text=f'You Should Give {forth} mg/{fifth}hrs',font=global_font)
    label4.pack()

    def button_click():
        frame.destroy()

    space3.pack()
    space4.pack()

    quit_button = tk.Button(frame, command=button_click, text="Exit",font=global_font)
    quit_button.pack()

    frame.mainloop()
