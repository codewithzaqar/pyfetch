import platform

def get_ascii_art():
    """Return ASCII art based on the operating system."""
    os_name = platform.system().lower()
    ascii_arts = {
        "linux": """
              &&&&&&       
              &&&&&&&&      
              &&&&&&&&      
              &  &&&&      
              &&&&  &&&     
            &&      &&&&   
            &&        &&&&  
          &&         &&&&  
          &&&&       &&&&&  
        &     &&     &    &&
        &      &&&&&&&    & 
          &&&&&&  &&& &&
        """,
        "windows": """

                     Xxxxxxxxxxxxxxx 
          xxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
         xxxxxxxxxxxxxxxxxxxxxxxxxxx 
                     Xxxxxxxxxxxxxxx    

        """,
        "darwin": """
                            &         
                        &&&&&        
                      &&&&&&         
                      &&&&&&          
              &&&&&  &&&& &&&&&      
            &&&&&&&&&&&&&&&&&&&&&&&   
          &&&&&&&&&&&&&&&&&&&&&&&&&&  
        &&&&&&&&&&&&&&&&&&&&&&&&&    
        &&&&&&&&&&&&&&&&&&&&&&&&     
        &&&&&&&&&&&&&&&&&&&&&&&&     
        &&&&&&&&&&&&&&&&&&&&&&&&     
        &&&&&&&&&&&&&&&&&&&&&&&&&    
          &&&&&&&&&&&&&&&&&&&&&&&&&&  
          &&&&&&&&&&&&&&&&&&&&&&&&&& 
          &&&&&&&&&&&&&&&&&&&&&&&&&  
            &&&&&&&&&&&&&&&&&&&&&&   
              &&&&&&&&&&&&&&&&&&&     
                &&&&       &&&&       
        """
    }
    return ascii_arts.get(os_name, 
    """  
                 Xxxxxxxxxxxxxxx 
      xxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
     xxxxxxxxxxxxxxxxxxxxxxxxxxx 
                 Xxxxxxxxxxxxxxx       
    """)