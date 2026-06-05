# Snowman ASCII Art stages (7 stages for smoother transition)
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     (___)
    """,
    # Stage 1: Snowman starts melting - loses base
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    # Stage 2: Loses bottom body
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    # Stage 3: Only head and upper body
    """
      ___  
     /___\\ 
     (o o) 
    """,
    # Stage 4: Head starts melting
    """
      ___  
     /____\\
    """,
    # Stage 5: Almost gone
    """
      __
     /  \\
    """,
    # Stage 6: Snowman completely melted
    """
    *  .  *  .
    .  *  .  *
    (puddle...)
    """
]