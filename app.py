import streamlit as st

# Page config
st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

# Custom CSS styling
st.markdown('''
    <style>
    body {
        background: linear-gradient(to right, #f5b7b1, #f1948a);  /* Soft gradient for the background */
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
    }

    .title {
        text-align: center;
        font-size: 4em;
        font-weight: bold;
        color: #f39c12;  /* Golden yellow */
        text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
    }

    .turn-text {
        text-align: center;
        font-size: 2em;
        color: #fff;
        margin-bottom: 20px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
    }

    .game-container {
        background-color: #2c3e50;
        border-radius: 15px;
        padding: 40px;
        width: 480px;
        margin: auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        position: relative;
    }

    .button-cell {
        height: 150px;
        width: 150px;
        font-size: 80px;
        font-weight: bold;
        background-color: #2980b9;  /* Blue color for the cells */
        border: none;
        border-radius: 12px;
        color: white;
        margin: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    .button-cell:hover {
        background-color: #3498db;
        transform: scale(1.1);
    }

    .button-cell:active {
        transform: scale(0.9);
    }

    .restart-button {
        font-size: 20px;
        padding: 10px 30px;
        border-radius: 10px;
        margin-top: 30px;
        background-color: #27ae60;  /* Green restart button */
        color: white;
        border: none;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    .restart-button:hover {
        background-color: #2ecc71;
    }

    .winner-message {
        font-size: 30px;
        color: white;
        background-color: rgba(0, 0, 0, 0.8);
        padding: 30px;
        border-radius: 15px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: none;
        text-align: center;
        width: 350px;
    }

    .close-btn {
        position: absolute;
        top: 5px;
        right: 10px;
        color: rgb(242, 239, 245);
        font-size: 25px;
        cursor: pointer;
    }

    </style>
''', unsafe_allow_html=True)

# Game title
st.markdown('<div class="title">🎮 Tic-Tac-Toe Game</div>', unsafe_allow_html=True)

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [["_" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

def check_winner(board):
    for i in range(3):
        if board[i][0] != "_" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "_" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] != "_" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "_" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != "_" for row in board for cell in row)

def reset_game():
    st.session_state.board = [["_" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

# Game status
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif st.session_state.game_over:
    st.warning("It's a draw!")
else:
    st.markdown(f'<div class="turn-text">Player {st.session_state.current_player}\'s turn</div>', unsafe_allow_html=True)

# Game board
st.markdown('<div class="game-container">', unsafe_allow_html=True)
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell_value = st.session_state.board[i][j]
        cell_display = cell_value if cell_value != "_" else " "
        button_label = f"{cell_display}"

        if cols[j].button(button_label, key=f"{i}-{j}", help="Click to play", type="secondary"):
            if not st.session_state.game_over and st.session_state.board[i][j] == "_":
                st.session_state.board[i][j] = st.session_state.current_player
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                    st.session_state.game_over = True
                elif is_draw(st.session_state.board):
                    st.session_state.game_over = True
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
st.markdown('</div>', unsafe_allow_html=True)

# Restart button
st.markdown('<br>', unsafe_allow_html=True)
st.button("🔁 Restart Game", on_click=reset_game)
