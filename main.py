import divin

divin.welcome()
q = divin.question()
yaos = divin.throw_coins()
yaocode = divin.read_yao(yaos)

questiontitle = f'關於你的問題 :  {q}'
print(questiontitle)

titletext = divin.get_titletext()
file_titles,yao_code_list,yao_symbol_list = divin.get_fT_yC_yS(titletext)

answer = divin.answer(file_titles,yao_code_list,yao_symbol_list,yaocode)
print(answer)

text = divin.anstext(questiontitle,answer)
divin.save_file(text)