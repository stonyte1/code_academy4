import PySimpleGUI as sg

def window(quote, index, authors):
    loses = 0
    sg.theme("DarkAmber")
    layout = [
        [sg.Text('Guess the author of the quote', justification='center')],
        [sg.Text(quote)],
        [sg.Combo(authors, key='guess')],
        [sg.Button('Confirm answer'),
        sg.Button('New quote')]
    ]

    window = sg.Window('Quotes game', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Confirm answer':
            player_guess = values['guess'] 
            if authors.index(player_guess) == index:
                win()
            else:
                loses += 1
                if loses == 1:
                    lose1(authors[index])
                elif loses == 2:
                    lose2(authors[index])
                elif loses == 3:
                    lose3(authors[index])
        elif event == 'New quote':
            confirm = sg.popup_ok_cancel(f'Are you sure you want new wuote? You still have {3 - loses} guesses', title='New quote')
            if confirm == 'OK':
                return True
            elif confirm == 'CANCEL':
                continue
            
def win():
    sg.popup('You won!', title='Win')

def lose1(author):
    initials = ''
    words = author.split()
    for word in words:
        initials += word[0].upper() 
    sg.theme("DarkAmber")
    layout = [
        [sg.Text('Author initials: ')],
        [sg.Text(initials)]
    ]

    window = sg.Window('Wrong answer', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

def lose2(author):
    authors_info = {
        'Albert Einstein': 'March 14, 1879 in Ulm, Germany', 
        'J.K. Rowling': 'July 31, 1965 in Yate, South Gloucestershire, England, The United Kingdom',
        'Jane Austen': 'December 16, 1775 in Steventon Rectory, Hampshire, The United Kingdom',
        'Marilyn Monroe': 'June 01, 1926 in The United States',
        'André Gide': 'November 22, 1869 in Paris, France',
        'Thomas A. Edison': 'February 11, 1847 in Milan, Ohio, The United States',
        'Eleanor Roosevelt': 'October 11, 1884 in The United States',
        'Steve Martin': 'August 14, 1945 in Waco, Texas, The United States'
        }
    
    author_info = authors_info.get(author)
    
    sg.theme("DarkAmber")
    layout = [
        [sg.Text('Author info: ')],
        [sg.Text(author_info)]
    ]

    window = sg.Window('Wrong answer', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

def lose3(author):
    
    sg.theme("DarkAmber")
    layout = [
        [sg.Text('Answer: ')],
        [sg.Text(author)],
        [sg.Text('Try again')]
    ]

    window = sg.Window('Wrong answer', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break


