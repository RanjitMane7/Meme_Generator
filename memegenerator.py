#Copy for Lappy

'''
********* Todo's *******
   1. Introduce GIT for ver controlling
   2. Fix issue with high resolution images.
   3. add functionality to read the images and quotes and merge them
   4. Save the generated image
   5. Move the used and defected quotes nad images from the source directories/files.

'''


from PIL import Image, ImageDraw, ImageFont
import textwrap
import random, os, time

def generate_img(img_path, quote_text = 'Not passed showing default', author_text = 'unKNown', font_path = 'impact/Impact.ttf') :
    #Path to files
    #print(quote_text)
    Img_path = img_path
    Font_ttf_path = font_path
    #Font_ttf_path = 'impact/Impact.ttf'
    #quote = 'We must respect the other fellows religion, but only in the sense and to the extent that we respect his theory that his wife is beautiful and his children smart.' 
    quote = quote_text
    author = author_text
    #print(author)

    #size_to_font = int(len(quote)/5)

    #Creating objects

    img_obj = Image.open(Img_path)
    #Storing the img attributes
    img_width, img_height = img_obj.size

    img_draw_obj = ImageDraw.Draw(img_obj)
    #img_font_obj = ImageFont.truetype(font=Font_ttf_path,size=int(img_height / size_to_font))   ## Cant get the correct size here!
    img_font_obj = ImageFont.truetype(font=Font_ttf_path,size=125)   ## Cant get the correct size here!

    #wrapping the text
    char_width, char_height = img_font_obj.getsize('A')
    img_char_width = int(img_width / char_width)

    quote_wrapped = textwrap.wrap(quote,width=img_char_width)

    #print(quote_wrapped)


    #Writing the text on Image
    '''
    for i in quote_wrapped :
        y += text_height
        x = int((img_width - (text_width * len(i))) / 2)
        print(x,len(i))
        img_draw_obj.text((x,y), i, fill='white', font=img_font_obj)
    '''

    '''
    ##########     For thin boundry     ############
    y = (img_height - char_height * len(quote_wrapped)) / 2 - char_height
    for i in quote_wrapped :
        line_width, line_height = img_font_obj.getsize(i)
        print(line_width,img_width)
        x = (img_width - line_width) / 2
        #print(x,len(i))
        img_draw_obj.text((x-1,y), i, fill='black', font=img_font_obj)
        img_draw_obj.text((x+1,y), i, fill='black', font=img_font_obj)
        img_draw_obj.text((x,y-1), i, fill='black', font=img_font_obj)
        img_draw_obj.text((x,y+1), i, fill='black', font=img_font_obj)
        y += line_height
    #################################################    
    '''


    ##########     For thin boundry     ############
    y = (img_height - char_height * len(quote_wrapped)) / 2 - char_height
    for i in quote_wrapped :
        line_width, line_height = img_font_obj.getsize(i)
        #print(line_width,img_width)
        x = (img_width - line_width) / 2
        #print(x,len(i))
        img_draw_obj.text((x-2,y-2), i, fill='black', font=img_font_obj)
        img_draw_obj.text((x+2,y-2), i, fill='black', font=img_font_obj)
        img_draw_obj.text((x-2,y+2), i, fill='black', font=img_font_obj)
        img_draw_obj.text((x+2,y+2), i, fill='black', font=img_font_obj)
        y += line_height
    #################################################


    y = (img_height - char_height * len(quote_wrapped)) / 2 - char_height
    #print(y)
    for i in quote_wrapped :
        line_width, line_height = img_font_obj.getsize(i)
        #print(line_width,img_width)
        x = (img_width - line_width) / 2
        #print(x,len(i))
        img_draw_obj.text((x,y), i, fill='white', font=img_font_obj)
        y += line_height



    #print(y)

    #Printing Author of the quote OUTLINE - Black
    #img_font_obj = ImageFont.truetype(font=Font_ttf_path,size=int(img_height / (size_to_font + 5)))
    img_font_obj = ImageFont.truetype(font=Font_ttf_path,size=68)
    auth_width, auth_height = img_font_obj.getsize(author)
    x = (img_width - auth_width) / 2 - char_width
    img_draw_obj.text((x-1,y-1), '- ' + author, fill='black', font=img_font_obj)
    img_draw_obj.text((x+1,y-1), '- ' + author, fill='black', font=img_font_obj)
    img_draw_obj.text((x-1,y+1), '- ' + author, fill='black', font=img_font_obj)
    img_draw_obj.text((x+1,y+1), '- ' + author, fill='black', font=img_font_obj)

    #Printing Author of the quote
    #img_font_obj = ImageFont.truetype(font=Font_ttf_path,size=int(img_height / (size_to_font + 5)))
    #img_font_obj = ImageFont.truetype(font=Font_ttf_path,size=68)
    auth_width, auth_height = img_font_obj.getsize(author)
    x = (img_width - auth_width) / 2 - char_width
    img_draw_obj.text((x,y), '- ' + author, fill='white', font=img_font_obj)
    

    #Displaying the final image.
    #img_obj.show()
    img_obj.save( 'Product' + '/OK_' + img_obj.filename.split(sep='/')[1])
    img_obj.close()
    
    ######### End of the Function ##########


############# Set the Paths here, Manual Entries ####################
font_to_fun = 'impact/impact.ttf'
Images_dir_path = 'D:\Downloaded\Shutterstock\5-Nature'
Quotes_file_path = 'all_quotes.txt'
#####################################################################


quotes_file = open(Quotes_file_path)
quotes_list = quotes_file.readlines()
quotes_file.close()
quotes_list_formatted = []

for i in quotes_list :
    quotes_list_formatted.append(i.rsplit(sep='|'))


selected_100 = random.choices(quotes_list_formatted,k=100)

#print(selected_100)

image_list = random.choices(os.listdir('Images_dir'),k=90)
#print(image_list)

print('Started at :', time.ctime())

for i in range(len(image_list)) :
    if selected_100[i][1] == '' or len(selected_100[i][1]) > 420:
        print('Skipped : ' + image_list[i])
        continue
    
    #print('Images_dir/' + image_list[i], selected_100[i][1], selected_100[i][2])
    generate_img('Images_dir/' + image_list[i], selected_100[i][1], selected_100[i][2],)#font_to_fun)
    if i > 90 :
        exit()

print('Ended at :', time.ctime())
