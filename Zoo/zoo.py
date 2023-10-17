print("I love animals")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")

camel = r"""
The camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that!"""

rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y    
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks fine!"""

deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'

 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           |  |           | |   | |
           |  |           | |   | |
           |  |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Pretty good!"""

bat = r"""
The bat habitat...
 /\                 /\
/ \'._   (\_/)   _.'/ \
|.''._'--(o.o)--'_.''.|
 \_ / ;=/ " \=; \ _/
   \__| \___/ |__/
        \(_|_)/
         " ` "
It's doing fine."""

lion = r"""
The lion habitat...
                                     , w.
                                , YWMMw, M,
                              'MMMMMw,wMWmW,
_. - ""        '''           YP"WMMMMMMMMMb,
                 .-'  __.'                  .'     MMMMW^WMMMM;
    _,         .' .-'";   `,    /`    .--""       :MMM[==MWMW^;
 ,mM^"      ,-' .'   /     ;    ;    /     ,      MMMMb_wMW" @\
,MM:.     .' .-'   .'      ;    `\   ;      `,    MMMMMMMW `"=./`-,
WMMm__,-'.' .`    /       _.\     F''' - +,, ;_, _.dMMMMMMMM[, _ / ` = _}
"^MP__.-'    ,-'   _.-""   `-,    ;    \    ; ;MMMMMMMMMMW^``; __|
            /    .'     '-,  ;      \      )  `{  \  `
           /   .'         /  ;     .`    /
          /   Y,          ', (-,=,_{     ;
          (--, )            ',_/`)  \/"")
The lion is roaring!"""

goose = r"""
The goose habitat...
                                          _
                                      ,-"" "".
                                    ,'  ____  `.
                                  ,'  ,'    `.  `._
         (`.         _..--.._   ,'  ,'        \    \
        (`-.\    .-""        ""'   /          (  d _b
       (`._  `-"" ,._             (            `-(   \
       <_  `     (  <`<            \              `-._\
        <`-       (__< <            :
         (__        (_<_<           ;
    ------------------------------------------------------
Beautiful!"""

animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    print("Please enter the number of the habitat you would like to view:")
    user_input = input("> ")
    if user_input == 'q':
        print("See you later!")
        break
    elif user_input.isdigit() and 0 <= int(user_input) <= 5:
        print(animals[int(user_input)])
        print("You've reached the end of the program.")
    else:
        print("Enter the correct number. Try from 0 to 5.")
