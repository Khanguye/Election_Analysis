print("Select your choice: r (Rock), p (Paper), s (Scissor)")
player_1 = input("Player 1:")
player_2 = input("Player 2:")

if (player_1 == player_2):
    print(f"tied")
elif (player_1 == "r" and player_2=='s') or (player_1 == "p" and player_2=='r') or (player_1 == "s" and player_2=='p'):
    print(f"player 1 - won")
else:
    print(f"player 1 - lost")
