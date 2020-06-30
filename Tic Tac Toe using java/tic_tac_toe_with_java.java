//=============== TIC TAC TOE USING JAVA =================



import java.util.Scanner;

// Main class
public class tic_tac_toe {
	
	  // Main method
	  public static void main(String[] args) {

		  play_game();
		}
	  
//     METHODS :~                                          
//------------------------------------------------------------------------------------------------------------------------------
		// defining play_game() method
		static void play_game() {
			display_board();
			
			while(game_still_going) {
				System.out.println(current_player + " 's turn");
				handle_turn();
				game_ended();
				flip_players();
			}
		}	  
	
//-------------------------------------------------------------------------------------------------------------------------------	
    //initializing some variables
	static String current_player = "X";
	static boolean game_still_going = true;
	static Double position;

//-------------------------------------------------------------------------------------------------------------------------------
	// creating game board using multidimentional array
	static String[][] game_board={{"_","_","_"},
	                              {"_","_","_"},
	                              {"_","_","_"}} ;
	
//--------------------------------------------------------------------------------------------------------------------------------	
	// method for displaying the game board
	static void display_board()
	{
		System.out.println(game_board[0][0]+" | "+game_board[0][1]+" | "+game_board[0][2] + "        1   2   3");
		System.out.println(game_board[1][0]+" | "+game_board[1][1]+" | "+game_board[1][2] + "        4   5   6");
		System.out.println(game_board[2][0]+" | "+game_board[2][1]+" | "+game_board[2][2] + "        7   8   9");
	}


//----------------------------------------------------------------------------------------------------------------------------------	
	//defining a method to check the winner, win()
	static void game_ended() {
		 if((game_board[0][0] == "X" && game_board[0][1] == "X" && game_board[0][2] == "X") ||
			(game_board[0][0] == "O" && game_board[0][1] == "O" && game_board[0][2] == "O")	){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 if((game_board[1][0] == "X" && game_board[1][1] == "X" && game_board[1][2] == "X") ||
				 (game_board[1][0] == "O" && game_board[1][1] == "O" && game_board[1][2] == "O")){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 if((game_board[2][0] == "X" && game_board[2][1] == "X" && game_board[2][2] == "X") ||
				 (game_board[2][0] == "O" && game_board[2][1] == "O" && game_board[2][2] == "O")){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 if((game_board[0][0] == "X" && game_board[1][0] == "X" && game_board[2][0] == "X") ||
				 (game_board[0][0] == "O" && game_board[1][0] == "O" && game_board[2][0] == "O")){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 if((game_board[0][1] == "X" && game_board[1][1] == "X" && game_board[2][1] == "X") ||
				 (game_board[0][1] == "O" && game_board[1][1] == "O" && game_board[2][1] == "O")){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 if((game_board[0][2] == "X" && game_board[1][2] == "X" && game_board[2][2] == "X") ||
				 (game_board[0][2] == "O" && game_board[1][2] == "O" && game_board[2][2] == "O")){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 if((game_board[0][0] == "X" && game_board[1][1] == "X" && game_board[2][2] == "X") ||
				 (game_board[0][0] == "O" && game_board[1][1] == "O" && game_board[2][2] == "O")){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 if((game_board[0][2] == "X" && game_board[1][1] == "X" && game_board[2][0] == "X") ||
				 (game_board[0][2] == "O" && game_board[1][1] == "O" && game_board[2][0] == "O")){
		 	System.out.println("Player " + current_player + " is the winner");
		 	game_still_going = false;
		 }
		 else if(game_board[0][0] != "_" && game_board[0][1] != "_" && game_board[0][2] != "_"
			  && game_board[1][0] != "_" && game_board[1][1] != "_" && game_board[1][2] != "_"
			  && game_board[2][0] != "_" && game_board[2][1] != "_" && game_board[2][2] != "_") 
		      {
					 System.out.println("It's a TIE !");
					 game_still_going = false;
		      }
	}
	

//---------------------------------------------------------------------------------------------------------------------------------
	// flipping players
	static void flip_players() {
		if(current_player == "X") 
			current_player = "O";
		else
			current_player = "X";
	}

//---------------------------------------------------------------------------------------------------------------------------------
	//taking input from the user
	static void input() {
        Scanner user_input = new Scanner(System.in);
        System.out.print("choose a position : ");
		position = Double.parseDouble(user_input.nextLine());
	}
	
//---------------------------------------------------------------------------------------------------------------------------------
	//taking input if the position is invalid
	static void input2() {
        Scanner valid_user_input = new Scanner(System.in);
        System.out.print("INVALID!! Choose another position : ");
		position = Double.parseDouble(valid_user_input.nextLine());
	}
	
//---------------------------------------------------------------------------------------------------------------------------------	
	// handling the turns
	static void handle_turn() {
		input();
		boolean x = true;
		
		while(x) {
		
		//displaying input in the game board after taking the position from the user
	    if(position == 1 && game_board[0][0]=="_"){
			game_board[0][0]=current_player;
			display_board();
			x = false; }
	    else if(position == 2 && game_board[0][1]=="_"){
			game_board[0][1]=current_player;
			display_board();
			x = false; }
	    else if(position == 3 && game_board[0][2]=="_"){
			game_board[0][2]=current_player;
			display_board();
			x = false; }
	    else if(position == 4 && game_board[1][0]=="_"){
			game_board[1][0]=current_player;
			display_board();
			x = false; }	
	    else if(position == 5 && game_board[1][1]=="_"){
			game_board[1][1]=current_player;
			display_board();
			x = false; }	
	    else if(position == 6 && game_board[1][2]=="_"){
			game_board[1][2]=current_player;
			display_board();
			x = false; }
	    else if(position == 7 && game_board[2][0]=="_"){
			game_board[2][0]=current_player;
			display_board();
			x = false; }
	    else if(position == 8 && game_board[2][1]=="_"){
			game_board[2][1]=current_player;
			display_board();
			x = false; }
	    else if(position == 9 && game_board[2][2]=="_"){
			game_board[2][2]=current_player;
			display_board();
			x = false; }
	    else {
	    	input2();
	         }
		    
	 }	

  }
	
//------------------------------------------------------------------------------------------------------------------------------	
	
}	
	
