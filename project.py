from flask import Flask, render_template, request
import game1
import game2
import game3
import game4
wins = [0,0,0,0]

app = Flask(__name__)

def check_no_official(guess):
        return check_no(guess)

@app.route('/')
def index():
        global wins
        reward = False
        if wins == [1,1,1,1]:
                reward = True
        return render_template('index.html', gif = reward)

@app.route('/fast')
def quickly():
        reward = True
        return render_template('index.html', gif = reward)

@app.route('/response_game1', methods=['POST'])
def response_game1():
        global wins
        guess1=request.form["guess1"]
        if guess1 not in ['1','2','3','4','5','6','7','8','9','10']:
                guess1=False
        else:
                game1.no_guess = game1.no_guess - 1
                if str(guess1) == str(game1.winning_guess):
                        game1.winning_1 = True
                        wins[0] = 1
        return render_template("game1.html", user_guess=guess1,winning_no=game1.winning_guess, current_guess=game1.no_guess, winning=game1.winning_1)

@app.route('/game1', methods=['POST', 'GET'])
def GuessTheNumber():
        game1.start()
        game1.no_guess = 3
        game1.winning_1 = False
        return render_template('game1.html', winning_no=game1.winning_guess, current_guess=game1.no_guess, winning=game1.winning_1)

@app.route('/game2', methods=['POST','GET'])
def BlackJack():
        game2.starting()
        return render_template('game2.html', w = game2.winner, c_card = game2.first_card, p_playing = game2.p_status, c_playing = game2.o_status, p_hand = game2.player_hand, c_hand = game2.opponent_hand)

@app.route('/response_game2', methods=['POST'])
def response_game2():
        global wins
        command=request.form["commands"]
        command=command.lower()
        if command == 'h':
                game2.player_hand, game2.p_status = game2.action_taken(game2.player_hand, game2.p_status)
        elif command == 's':
                game2.computer_deal()
                if game2.winner == 'p':
                        wins[1] = 1
        return render_template('game2.html', w = game2.winner, c_card = game2.first_card, p_playing=game2.p_status, c_playing=game2.o_status, p_hand=game2.player_hand, c_hand=game2.opponent_hand)

@app.route('/game3', methods=['POST','GET'])
def NuagthsCrosses():
        game3.setup()
        return render_template('game3.html', gameboard = game3.board, errorCheck = game3.invalidAns, winner=game3.winnerNC)

@app.route('/response_game3', methods=['POST'])
def game3_response():
        global wins
        co = request.form["coord"]
        game3.placement(co)
        if game3.invalidAns != True:
                game3.dumbComputer()
                game3.winnerCheck()
                if game3.winnerNC == 'p':
                        wins[2] = 1
        return render_template('game3.html', gameboard = game3.board, errorCheck = game3.invalidAns, winner=game3.winnerNC)

@app.route('/game4', methods=['POST','GET'])
def connect4():
        game4.cleaning()
        return render_template('game4.html', c4board = game4.board4, outside = game4.outOfBounds, connect4winner = game4.winnerC4, columnFull = game4.fullcolumn)

@app.route('/response_game4', methods=['POST'])
def game4_response():
        global wins
        LINE = request.form['straight']
        game4.drop(LINE)
        if (game4.fullcolumn != True) & (game4.outOfBounds != True):
                game4.C4wc()
                game4.computerTurn()
                game4.C4wc()
                if game4.winnerC4 == 'p':
                        wins[3] = 1
        return render_template('game4.html', c4board = game4.board4, outside = game4.outOfBounds, connect4winner = game4.winnerC4, columnFull = game4.fullcolumn)

if __name__ == "__main__":
        app.run(threaded=True)
