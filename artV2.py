#TODO: make some spooky sentences to type when player is fine, 10 is good [9/10]
SPOOKY_WORDS = [
  "What is a good game without serius consequences?",
  "Isn't it exciting? Dont worry, it will only get better...",
  "Next time might be very different...",
  "Kinda impressive... Expected you to run away on your first try",
  "The thrill of survival is intoxicating... but the fear of failure lingers.",
  "You made it through, but the echoes of the gun's spinning are still in your head.",
  "You survived, but the silence feels ominous, doesn’t it?",
  "You’re still standing, but the weight of the moment is heavy.",
  "For now, your files remain intact, but how long can that last?",
  "The difference between survivel and death has never seemed less controlled"
]



GUN_REGG = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   *@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   +@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@                                     
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@                                     
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@                                      
       @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   %@@@                                      
       @@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@                                      
        @@@@@     @@@@@@@@@@@@@@@@@@@@@@@     @@@@                                        
         @@@@@@     @@@@@@@@@@@@@@@@@@%     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_LOADED = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@....@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@@@@@@@@.000000.@@@@@@@@@@@@@@@   @@@@                                   
     @@@   @@@@@@@@@@@@.0000000000.@@@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@@.000000000000.@@@@@@@@@@@@   *@@@                                   
     @@@   @@@@@@@@@@.00000000000000.@@@@@@@@@@@   +@@@                                   
     @@@   @@@@@@@@@@.00000000000000.@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@.00000000000000.@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@@.000000000000.@@@@@@@@@@@@   @@                                     
      @@@   @@@@@@@@@@@.00000000000.@@@@@@@@@@@   @@@                                     
       @@@   @@@@@@@@@@@@.000000.@@@@@@@@@@@@@   @@@                                      
       @@@@   @@@@@@@@@@@@@....@@@@@@@@@@@@@@   %@@@                                      
       @@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@                                      
        @@@@@     @@@@@@@@@@@@@@@@@@@@@@@     @@@@                                        
         @@@@@@     @@@@@@@@@@@@@@@@@@%     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_UNLOADED = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@....@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@@@@@@@@........@@@@@@@@@@@@@@@   @@@@                                   
     @@@   @@@@@@@@@@@@............@@@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@@..............@@@@@@@@@@@@   *@@@                                   
     @@@   @@@@@@@@@@................@@@@@@@@@@@   +@@@                                   
     @@@   @@@@@@@@@@................@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@................@@@@@@@@@@@   @@@                                    
     @@@   @@@@@@@@@@@..............@@@@@@@@@@@@   @@                                     
      @@@   @@@@@@@@@@@............@@@@@@@@@@@@   @@@                                     
       @@@   @@@@@@@@@@@@........@@@@@@@@@@@@@   @@@                                      
       @@@@   @@@@@@@@@@@@@....@@@@@@@@@@@@@@   %@@@                                      
       @@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@                                      
        @@@@@     @@@@@@@@@@@@@@@@@@@@@@@     @@@@                                        
         @@@@@@     @@@@@@@@@@@@@@@@@@%     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_ROTATING1 = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@@@@   @@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@..........@@@   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@@@............@@   *@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@..............@   +@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@................   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@................   @@@                                    
     @@@   .......@@@@@@@@@@@@@@@..............@   @@                                     
      @@@   .........@@@@@@@@@@@@@............@   @@@                                     
       @@@   .........@@@@@@@@@@@@@@........@@   @@@                                      
       @@@@   .........@@@@@@@@@@@@@@@....@@    %@@@                                      
       @@@@    .........@@@@@@@@@@@@@@@@@@     @@@@@                                      
        @@@@@     .....@@@@@@@@@@@@@@@@@@     @@@@                                        
         @@@@@@     ..@@@@@@@@@@@@@@@@@     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_ROTATING1_BL = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@@@@   @@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@.00000000.@@@   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@@@.0000000000.@@   *@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@.000000000000.@   +@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@.00000000000000.   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@.00000000000000.   @@@                                    
     @@@   .......@@@@@@@@@@@@@@@.000000000000.@   @@                                     
      @@@   .........@@@@@@@@@@@@@.0000000000.@   @@@                                     
       @@@   .........@@@@@@@@@@@@@@.000000.@@   @@@                                      
       @@@@   .........@@@@@@@@@@@@@@@....@@    %@@@                                      
       @@@@    .........@@@@@@@@@@@@@@@@@@     @@@@@                                      
        @@@@@     .....@@@@@@@@@@@@@@@@@@     @@@@                                        
         @@@@@@     ..@@@@@@@@@@@@@@@@@     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_ROTATING1_PL = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@@@@   @@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@@@..........@@@   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@@@............@@   *@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@@..............@   +@@@                                   
     @@@   @@@@@@@@@@@@@@@@@@@@@................   @@@                                    
     @@@   @@@@@@@@@@@@@@@@@@@@@................   @@@                                    
     @@@   .......@@@@@@@@@@@@@@@..............@   @@                                     
      @@@   00000000.@@@@@@@@@@@@@............@   @@@                                     
       @@@   00000000.@@@@@@@@@@@@@@........@@   @@@                                      
       @@@@   00000000.@@@@@@@@@@@@@@@....@@    %@@@                                      
       @@@@    00000000.@@@@@@@@@@@@@@@@@@     @@@@@                                      
        @@@@@     0000.@@@@@@@@@@@@@@@@@@     @@@@                                        
         @@@@@@     ..@@@@@@@@@@@@@@@@@     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_ROTATING2 = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@....@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                   
     @@@   @@@@..........@@@@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@@............@@@@@@@@@@@@@@@@@@@@@@   *@@@                                   
     @@@   @@..............@@@@@@@@@@@@@@@@@@@@@   +@@@                                   
     @@@   @................@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @................@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@..............@@@@@@@@@@@@@@@......   @@                                     
      @@@   @@............@@@@@@@@@@@@.........   @@@                                     
       @@@   @@@........@@@@@@@@@@@@@.........   @@@                                      
       @@@@   @@@@....@@@@@@@@@@@@@@........    %@@@                                      
       @@@@    @@@@@@@@@@@@@@@@@@@@.......     @@@@@                                      
        @@@@@     @@@@@@@@@@@@@@@@@@.....     @@@@                                        
         @@@@@@     @@@@@@@@@@@@@@@@@..     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_ROTATING2_BL = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@....@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                   
     @@@   @@@@..........@@@@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@@............@@@@@@@@@@@@@@@@@@@@@@   *@@@                                   
     @@@   @@..............@@@@@@@@@@@@@@@@@@@@@   +@@@                                   
     @@@   @................@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @................@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@..............@@@@@@@@@@@@@@@......   @@                                     
      @@@   @@............@@@@@@@@@@@@.00000000   @@@                                     
       @@@   @@@........@@@@@@@@@@@@@.00000000   @@@                                      
       @@@@   @@@@....@@@@@@@@@@@@@@.0000000    %@@@                                      
       @@@@    @@@@@@@@@@@@@@@@@@@@.000000     @@@@@                                      
        @@@@@     @@@@@@@@@@@@@@@@@@.0000     @@@@                                        
         @@@@@@     @@@@@@@@@@@@@@@@@..     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

GUN_ROTATING2_PL = """
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         @@@@@@@@                                                         
                         *@@@@@@@                                                         
                         @@@@@@@@                                                         
                    #@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@                                                  
                   @@@@@@@@@@@@@@@@@@@@@@                                                 
                @@@@@                  @@@@@                                              
             @@@@@      @@@@@@@@@@@*      @@@@@@                                          
           @@@@@    @@@@@@@@@@@@@@@@@@@@*  @@@@@#                                         
         @@@@:@@#@@@@@                %@@@@@@ @@@                                         
         @@@ #@@@@*      @@@@@@@@@@       @@@@@@#                                         
         @@@@@@@    @@@@@@@@@@@@@@@@@@@     @@@@+                                         
         %@@@@    %@@@@@@@@@@@@@@@@@@@@@@#    @@@+                                        
         @@@%   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                       
        @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@                                      
       @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@                                    
      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                                    
     @@@@  @@@@@@@....@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                   
     @@@   @@@@.00000000.@@@@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@@.0000000000.@@@@@@@@@@@@@@@@@@@@@@   *@@@                                   
     @@@   @@.000000000000.@@@@@@@@@@@@@@@@@@@@@   +@@@                                   
     @@@   @.00000000000000.@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @.00000000000000.@@@@@@@@@@@@@@@@@@@@   @@@                                    
     @@@   @@.000000000000.@@@@@@@@@@@@@@@......   @@                                     
      @@@   @@.0000000000.@@@@@@@@@@@@.........   @@@                                     
       @@@   @@@.000000.@@@@@@@@@@@@@.........   @@@                                      
       @@@@   @@@@....@@@@@@@@@@@@@@........    %@@@                                      
       @@@@    @@@@@@@@@@@@@@@@@@@@.......     @@@@@                                      
        @@@@@     @@@@@@@@@@@@@@@@@@.....     @@@@                                        
         @@@@@@     @@@@@@@@@@@@@@@@@..     @@@@@                                         
          @@@@@@@      @@@@@@@@@@@@       @@@@@                                           
               @@@@                    @@@@@                                              
                 %@@@@@@@@+     +@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@@@@@                                                 
                    @@@@@@@@@@@@@@@@@ @@%                                                 
                    @@@@@          @@.@@#                                                 
                    @@@@@          @@+@@%                                                 
                    @@@@@          @@#@@@                                                 
                    @@@@@  @@@@@@@@@@%@@@                                                 
                    @@@@@ %@@@@@@@@@ =@@@                                                 
                    %@@@@@@@@@@@@@@@@@@@                                                  
                      +@@@@@@@@@@@@*                                                      
"""

