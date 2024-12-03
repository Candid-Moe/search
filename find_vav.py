#
#   find_vav.py : Find consecutives words starting with the vav.
#
#   File names are hardcoded. Run the code in the directory where
#   the files are with
#
#       python find_vav.py
#
#   Note: First time working with Unicode multiple languages text,
#   so probably there are errors.
#

maqaf = chr(0x05BE)
vav = chr(1493)
mark1 = '\u202a'  # Unicode marks delimiting lenguages
mark2 = '\u202c'
prefix_comment = "xxxx"

#   Books comes from https://www.tanach.us/Pages/Technical.html#zipfiles
#   ("Tanach.txt.zip" format)

books = ['Genesis.txt', 'Exodus.txt', 'Leviticus.txt', 'Numbers.txt', 'Deuteronomy.txt']

printed = False         # Have we printed the "Chapter xx" yet ?

for book in books:

    #   Print book name
    print()
    print(book[:-4])
    print()

    with (open(book, "r") as archivo):
        #
        #   We accumulate matching words in this list and print it
        #   after adding the third word.
        #
        lista = []

        #   Processing the book line by line

        for line in archivo.readlines():
            #
            #   file include lines starting with "xxxx ", from where
            #   we get the Chapter,
            #
            line = line.strip()
            line = line.replace(maqaf, " ")
            line = line.replace(mark1, " ")
            line = line.replace(mark2, " ")

            words = line.split()

            if words[0] == prefix_comment:
                if "Chapter" in line:
                    #
                    #   A line like "xxxx  Chapter 1   (31 verses)"
                    #
                    chapter = words[2]
                    printed = False
            else:
                #
                #   A line from the book in the form
                #   'word ... word word chapter: verso'
                #
                verso = words[1]

                #   Process word by word
                for word in words[3:]:
                    if word[0] == vav:
                        #
                        #   Add the word starting with vav to the list
                        #
                        lista.append(word)
                        if len(lista) == 3:
                            #
                            #   We have three consecutives words, print it
                            #
                            if not printed:
                                print("Chapter ", chapter)
                                printed = True

                            print(f" {verso} :{chapter}", ' '.join(lista))
                            #
                            #   Reset the list to start anew
                            #
                            lista = []
                    else:
                        #
                        #   Not a word starting with vav, delete the list
                        #
                        lista = []
        print("------------------ ")