import random

pieceScore = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1 }

KNIGHT_SCORES = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.2, 0.5, 0.6, 0.6, 0.6, 0.6, 0.5, 0.2],
                 [0.2, 0.5, 0.6, 0.7, 0.7, 0.6, 0.5, 0.2],
                 [0.2, 0.5, 0.6, 0.7, 0.7, 0.6, 0.5, 0.2],
                 [0.2, 0.5, 0.6, 0.6, 0.6, 0.6, 0.5, 0.2],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

BISHOP_SCORES = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

ROOK_SCORES = [[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
               [0.5, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.5],
               [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
               [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
               [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
               [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
               [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
               [0.2, 0.2, 0.2, 0.5, 0.5, 0.2, 0.2, 0.2]]

QUEEN_SCORES = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

PAWN_SCORES = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
               [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
               [0.2, 0.2, 0.3, 0.4, 0.4, 0.3, 0.2, 0.2],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.2, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2],
               [0.2, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.2],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

PIECE_POSITION_SCORE = {
    "wp": PAWN_SCORES,
    "bp": PAWN_SCORES[::-1],
    "wN": KNIGHT_SCORES,
    "bN": KNIGHT_SCORES[::-1],
    "wB": BISHOP_SCORES,
    "bB": BISHOP_SCORES[::-1],
    "wR": ROOK_SCORES,
    "bR": ROOK_SCORES[::-1],
    "wQ": QUEEN_SCORES,
    "bQ": QUEEN_SCORES[::-1]
}

CHECKMATE = 1000
STALEMATE = 0
DEPTH  = 3


def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves) -1 )]

def findbestMoveMinMaxNoRecursion(gs, validMoves):
    turnMultiplier = 1 if gs.whiteToMove else -1
    opponentMinMaxScore = CHECKMATE
    bestPlayerove = None
    random.shuffle(validMoves)
    for playerMove in validMoves:
        gs.makeMove(playerMove)
        opponentsMoves = gs.getValidMoves()
        if gs.stalemate:
            opponentMaxScore = STALEMATE
        elif gs.checkmate:
            opponentMaxScore = -CHECKMATE
        else:
            opponentMaxScore = -CHECKMATE
            for opponentsMove in opponentsMoves:
                gs.makeMove(opponentsMove)
                if gs.checkmate:
                    score = CHECKMATE
                elif gs.stalemate:
                    score = STALEMATE
                else:
                    score = -turnMultiplier * scoreBoard(gs.board)
                if score > opponentMaxScore:
                    maxScore = score
                    bestPlayerMove = playerMove
                gs.undoMove()
        if opponentMaxScore < opponentMinMaxScore :
            opponentMinMaxScore = opponentMaxScore 
            bestPlayerove = playerMove
        gs.undoMove()
    return bestPlayerMove

def findBestMove(gs,  validMoves, returnQueue):
    global nextMove, counter 
    nextMove = None
    random.shuffle(validMoves)
    counter = 0
    #findMoveMinMax(gs, validMoves, DEPTH, gs.whiteToMove)
    #findMoveNegaMax(gs, validMoves, DEPTH, 1 if gs.whiteToMove else)
    findMoveNegaMaxAlphaBeta(gs, validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    returnQueue.put(nextMove)


def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
    global nextMove, counter
    counter += 1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)

    
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(gs, nextMoves, depth - 1, -beta, -alpha, -turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        gs.undoMove()
        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta:
            break
    return maxScore

def scoreBoard(gs):
    if gs.checkmate:
        if gs.whiteToMove:
            return -CHECKMATE
        else:
            return CHECKMATE
    elif gs.stalemate:
        return STALEMATE
    
    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            if square != '--':
                piecePositionScore = 0
                if square[1] != "K":
                    if square[1] == "p":
                        piecePositionScore = PIECE_POSITION_SCORE[square][row][col]


                if square[0] == 'w':
                    score += pieceScore[square[1]] + piecePositionScore
                elif square[0] == 'b':
                    score -= pieceScore[square[1]] + piecePositionScore
        
    return score     





