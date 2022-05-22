class Display: 
    #Please create a variable that is public called "tries" and set it equal to 4
    def display_para(tries): 
        stages = [
            """
             ___
            /___\
            \   /
             \ /
              O
             /|\
             / \   

            """,
            """
             
            /___\
            \   /
             \ /
              O
             /|\
             / \   

            """,
            """
             
            
            \   /
             \ /
              O
             /|\
             / \   

            """,
            """
             
        
            
             \ /
              O
             /|\
             / \   

            """,
            """
             
              x
             /|\
             / \   

            """,
        ]
        return stages[tries]

