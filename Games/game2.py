import random
player_hand = 0
first_card = 0
opponent_hand = 0
p_status = True
o_status = True
winner = 'n'

def starting():
    global player_hand, first_card, opponent_hand, p_status, o_status, winner
    winner = 'n'
    player_hand = random.randint(1,11) + random.randint(1,11)
    p_status = check(player_hand)
    opponent_hand = random.randint(1,11)
    first_card = opponent_hand
    opponent_hand = opponent_hand + random.randint(1,11)
    o_status = check(opponent_hand)
    return

def check(hand):
    if hand > 21:
        status = False
    else:
        status = True
    return status

def action_taken(hand, status):
    hand, status = deal_card(hand,status)
    return hand, status

def deal_card(current_hand, status):
    current_hand = current_hand + random.randint(1,11)
    x = check(current_hand)
    return current_hand, x

def computer_deal():
    global opponent_hand, o_status
    dealing = True
    while dealing == True:
        if opponent_hand <= 10:
            opponent_hand, o_status=deal_card(opponent_hand, o_status)
        elif (opponent_hand > 10) & (opponent_hand <= 12):
            if random.randint(1,2) == 1:
               opponent_hand, o_status=deal_card(opponent_hand, o_status)
            else:
               dealing = False
               break
        elif (opponent_hand > 12) & (opponent_hand <= 15):
            if random.randint(1,4) == 1:
               opponent_hand, o_status=deal_card(opponent_hand, o_status)
            else:
               dealing = False
               break
        elif (opponent_hand > 15) & (opponent_hand <= 18):
            if random.randint(1,8) == 1:
               opponent_hand, o_status=deal_card(opponent_hand, o_status)
            else:
               dealing = False
               break
        else:
            if random.randint(1,10) == 1:
               opponent_hand, o_status=deal_card(opponent_hand, o_status)
            else:
               dealing = False
               break
        if o_status == False:
            dealing = False
            return
    check_win()
    return

def check_win():
    global o_status, p_status, player_hand, opponent_hand, winner
    if o_status == False:
        winner = 'o'
    else:
        winner = 'p'
    c_score = 21 - opponent_hand
    p_score = 21 - player_hand
    if c_score > p_score:
        winner = 'p'
    else:
        winner = 'o'
