FasdUAS 1.101.10   ��   ��    k             l     ��  ��    &  USB Encryption Check - Mac OS X      � 	 	 @ U S B   E n c r y p t i o n   C h e c k   -   M a c   O S   X     
  
 l     ��������  ��  ��        l     ��  ��    0 *Detecting USB Drive through Folder Actions     �   T D e t e c t i n g   U S B   D r i v e   t h r o u g h   F o l d e r   A c t i o n s      l     ��������  ��  ��        l     ����  v         ��  1     ��
�� 
ascr��  ��  ��        l     ��������  ��  ��        l     ��  ��    H BCHECKING VOLUMES FOLDER FOR DRIVE CHANGES (START OF FOLDER ACTION)     �   � C H E C K I N G   V O L U M E S   F O L D E R   F O R   D R I V E   C H A N G E S   ( S T A R T   O F   F O L D E R   A C T I O N )       l     ��������  ��  ��      ! " ! l     �� # $��   # @ :on adding folder items to Volumes after receiving KINGSTON    $ � % % t o n   a d d i n g   f o l d e r   i t e m s   t o   V o l u m e s   a f t e r   r e c e i v i n g   K I N G S T O N "  & ' & l     ��������  ��  ��   '  ( ) ( l     �� * +��   * ( " List all Drives in Volumes folder    + � , , D   L i s t   a l l   D r i v e s   i n   V o l u m e s   f o l d e r )  - . - l    /���� / O     0 1 0 I  	 �� 2��
�� .sysoexecTEXT���     TEXT 2 m   	 
 3 3 � 4 4  l s   / V o l u m e s��   1 m     5 5�                                                                                      @ alis    <  Macintosh HD                   BD ����Terminal.app                                                   ����            ����  
 cu             	Utilities   &/:Applications:Utilities:Terminal.app/    T e r m i n a l . a p p    M a c i n t o s h   H D  #Applications/Utilities/Terminal.app   / ��  ��  ��   .  6 7 6 l     ��������  ��  ��   7  8 9 8 l     �� : ;��   : ' ! Set Variable to current username    ; � < < B   S e t   V a r i a b l e   t o   c u r r e n t   u s e r n a m e 9  = > = l    ?���� ? O     @ A @ r     B C B n     D E D 1    ��
�� 
pnam E 1    ��
�� 
curu C o      ���� 0 u U A m     F F�                                                                                  sevs  alis    \  Macintosh HD                   BD ����System Events.app                                              ����            ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��  ��  ��   >  G H G l     ��������  ��  ��   H  I J I l     �� K L��   K 4 . Assign Disk Name to current username variable    L � M M \   A s s i g n   D i s k   N a m e   t o   c u r r e n t   u s e r n a m e   v a r i a b l e J  N O N l   6 P���� P Q    6 Q R�� Q O     - S T S r   $ , U V U o   $ %���� 0 u U V n       W X W 1   ) +��
�� 
pnam X 4   % )�� Y
�� 
cdis Y m   ' ( Z Z � [ [  K I N G S T O N T m     ! \ \�                                                                                  MACS  alis    @  Macintosh HD                   BD ����
Finder.app                                                     ����            ����  
 cu             CoreServices  )/:System:Library:CoreServices:Finder.app/    
 F i n d e r . a p p    M a c i n t o s h   H D  &System/Library/CoreServices/Finder.app  / ��   R R      ������
�� .ascrerr ****      � ****��  ��  ��  ��  ��   O  ] ^ ] l     ��������  ��  ��   ^  _ ` _ l     ��������  ��  ��   `  a b a l     ��������  ��  ��   b  c d c l     �� e f��   e  CHECK IF DISK HAS DATA    f � g g , C H E C K   I F   D I S K   H A S   D A T A d  h i h l     ��������  ��  ��   i  j k j l  7 O l���� l Q   7 O m n�� m O   : F o p o r   > E q r q I  > C�� s��
�� .sysoexecTEXT���     TEXT s m   > ? t t � u u z d f   - h   / V o l u m e s / s b o h r   |   g r e p   ' / d e v / d i s k 2 s 2 '   |   a w k   ' { p r i n t   $ 3 } '��   r o      ���� 0 usbdata usbData p m   : ; v v�                                                                                      @ alis    <  Macintosh HD                   BD ����Terminal.app                                                   ����            ����  
 cu             	Utilities   &/:Applications:Utilities:Terminal.app/    T e r m i n a l . a p p    M a c i n t o s h   H D  #Applications/Utilities/Terminal.app   / ��   n R      ������
�� .ascrerr ****      � ****��  ��  ��  ��  ��   k  w x w l     ��������  ��  ��   x  y z y l     �� { |��   {  display dialog usbData    | � } } , d i s p l a y   d i a l o g   u s b D a t a z  ~  ~ l     ��������  ��  ��     � � � l     ��������  ��  ��   �  � � � l     �� � ���   �    Multi Line Comment START     � � � � 4   M u l t i   L i n e   C o m m e n t   S T A R T   �  � � � l     �� � ���   �  (*    � � � �  ( * �  � � � l     ��������  ��  ��   �  � � � l     �� � ���   � 4 .CHECK IF DISK IS ENCRYPTED BEFORE REFORMATTING    � � � � \ C H E C K   I F   D I S K   I S   E N C R Y P T E D   B E F O R E   R E F O R M A T T I N G �  � � � l     �� � ���   � 6 0################################################    � � � � ` # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # �  � � � l     �� � ���   � &  Check If Encryption is Completed    � � � � @ C h e c k   I f   E n c r y p t i o n   i s   C o m p l e t e d �  � � � l     ��������  ��  ��   �  � � � l  P � ����� � Q   P � � � � � k   S i � �  � � � O   S g � � � k   W f � �  � � � l  W W��������  ��  ��   �  � � � r   W d � � � I  W `�� ���
�� .sysoexecTEXT���     TEXT � b   W \ � � � m   W X � � � � �   d i s k u t i l   c s   l i s t � m   X [ � � � � � ( |   g r e p   ' C o n v e r s i o n '  ��   � o      ���� $0 encryptionstatus encryptionStatus �  ��� � l  e e��������  ��  ��  ��   � m   S T � ��                                                                                      @ alis    <  Macintosh HD                   BD ����Terminal.app                                                   ����            ����  
 cu             	Utilities   &/:Applications:Utilities:Terminal.app/    T e r m i n a l . a p p    M a c i n t o s h   H D  #Applications/Utilities/Terminal.app   / ��   �  � � � l  h h��������  ��  ��   �  � � � l  h h�� � ���   � , & encryptionStatus variable value check    � � � � L   e n c r y p t i o n S t a t u s   v a r i a b l e   v a l u e   c h e c k �  � � � l  h h�� � ���   � < 6display dialog "Encryption Status:" & encryptionStatus    � � � � l d i s p l a y   d i a l o g   " E n c r y p t i o n   S t a t u s : "   &   e n c r y p t i o n S t a t u s �  ��� � l  h h��������  ��  ��  ��   � R      ������
�� .ascrerr ****      � ****��  ��   � k   q � � �  � � � I  q x�� ���
�� .sysodlogaskr        TEXT � m   q t � � � � � � T h i s   U S B   D e v i c e   i s   n o t   e n c r y p t e d   a n d   c a n   n o t   s e c u r e l y   s t o r e   d a t a��   �  ��� � r   y � � � � m   y | � � � � �  F A I L � o      ���� $0 encryptionstatus encryptionStatus��  ��  ��   �  � � � l     ��������  ��  ��   �  � � � l     ��������  ��  ��   �  � � � l     � � ��   � 1 +If Encryption Status is Complete End Script    � � � � V I f   E n c r y p t i o n   S t a t u s   i s   C o m p l e t e   E n d   S c r i p t �  � � � l  �` ��~�} � Z   �` � ��| � � l  � � ��{�z � =  � � � � � o   � ��y�y $0 encryptionstatus encryptionStatus � m   � � � � � � � R                 C o n v e r s i o n   S t a t u s :               C o m p l e t e�{  �z   � k   � � � �  � � � I  � ��x ��w
�x .sysodlogaskr        TEXT � m   � � � � � � � p T h i s   U S B   D e v i c e   i s   E n c r y p t e d   a n d   c a n   s e c u r e l y   s t o r e   d a t a�w   �  � � � L   � ��v�v   �  ��u � l  � ��t�s�r�t  �s  �r  �u  �|   � k   �` � �  � � � l  � ��q�p�o�q  �p  �o   �  � � � I  � ��n ��m
�n .sysodlogaskr        TEXT � m   � � � � � � � � A n   U n e n c r y p t e d   U S B   D e v i c e   w a s   d e t e c t e d ,   b e g i n i n g   E n c r y p t i o n   p r o c e s s . .�m   �  � � � l  � ��l�k�j�l  �k  �j   �  � � � l  � ��i � ��i   � 6 0 Reformat Disk to Journaled GUID Partition Table    � � � � `   R e f o r m a t   D i s k   t o   J o u r n a l e d   G U I D   P a r t i t i o n   T a b l e �  � � � l  � ��h �h      Partition Disk    �    P a r t i t i o n   D i s k �  l  � ��g�f�e�g  �f  �e    l  � ��d�d   1 + LOGIC TO DECIDE WHAT TO DO IF USB HAS DATA    �		 V   L O G I C   T O   D E C I D E   W H A T   T O   D O   I F   U S B   H A S   D A T A 

 l  � ��c�c   2 ,############################################    � X # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  l  � ��b�a�`�b  �a  �`    Z   � ��_ l  � ��^�] =  � � o   � ��\�\ 0 usbdata usbData m   � � � 
 1 1 1 M i�^  �]   k   � �  l  � ��[�Z�Y�[  �Z  �Y    I  � ��X �W
�X .sysodlogaskr        TEXT  m   � �!! �"" V U S B   D e v i c e   h a s   n o   d a t a ,   r e - f o r m a t t i n g   d r i v e�W   #$# l  � ��V�U�T�V  �U  �T  $ %&% O   � �'(' k   � �)) *+* I  � ��S,�R
�S .sysoexecTEXT���     TEXT, m   � �-- �..  d i s k u t i l   l i s t�R  + /0/ I  � ��Q1�P
�Q .sysoexecTEXT���     TEXT1 m   � �22 �33 V d i s k u t i l   e r a s e D i s k   J H F S +   K I N G S T O N   G P T   d i s k 2�P  0 4�O4 I  � ��N5�M
�N .sysoexecTEXT���     TEXT5 m   � �66 �77 Z d i s k u t i l   p a r t i t i o n D i s k   d i s k 2   G P T   J H F S +   N e w   0 b�M  �O  ( m   � �88�                                                                                      @ alis    <  Macintosh HD                   BD ����Terminal.app                                                   ����            ����  
 cu             	Utilities   &/:Applications:Utilities:Terminal.app/    T e r m i n a l . a p p    M a c i n t o s h   H D  #Applications/Utilities/Terminal.app   / ��  & 9:9 l  � ��L�K�J�L  �K  �J  : ;<; l  � ��I=>�I  = ' ! Assign Disk Name after Re-Format   > �?? B   A s s i g n   D i s k   N a m e   a f t e r   R e - F o r m a t< @A@ O   � �BCB r   � �DED o   � ��H�H 0 u UE n      FGF 1   � ��G
�G 
pnamG 4   � ��FH
�F 
cdisH m   � �II �JJ  N e wC m   � �KK�                                                                                  MACS  alis    @  Macintosh HD                   BD ����
Finder.app                                                     ����            ����  
 cu             CoreServices  )/:System:Library:CoreServices:Finder.app/    
 F i n d e r . a p p    M a c i n t o s h   H D  &System/Library/CoreServices/Finder.app  / ��  A L�EL l  � ��D�C�B�D  �C  �B  �E  �_   k   � �MM NON l  � ��A�@�?�A  �@  �?  O PQP I  � ��>R�=
�> .sysodlogaskr        TEXTR m   � �SS �TT Z U S B   D e v i c e   h a s   d a t a ,   w i l l   n o t   r e - f o r m a t   d r i v e�=  Q UVU l  � ��<�;�:�<  �;  �:  V W�9W l  � ��8XY�8  X   End Data Check   Y �ZZ    E n d   D a t a   C h e c k�9   [\[ l  � ��7�6�5�7  �6  �5  \ ]^] l   � ��4_`�4  _ q k	-- Assign Disk Name after Re-Format		tell application "Finder"			set name of disk "New" to U		end tell    ` �aa � 	 - -   A s s i g n   D i s k   N a m e   a f t e r   R e - F o r m a t  	 	 t e l l   a p p l i c a t i o n   " F i n d e r "  	 	 	 s e t   n a m e   o f   d i s k   " N e w "   t o   U  	 	 e n d   t e l l  ^ bcb l  � ��3�2�1�3  �2  �1  c ded l  � ��0�/�.�0  �/  �.  e fgf l  � ��-hi�-  h %  Prompt for Encryption Password   i �jj >   P r o m p t   f o r   E n c r y p t i o n   P a s s w o r dg klk r   �mnm I  ��,op
�, .sysodlogaskr        TEXTo m   � �qq �rr b P l e a s e   c r e a t e   a   p a s s w o r d   f o r   t h i s   e x t e r n a l   d r i v e .p �+st
�+ 
dtxts m   � �uu �vv  t �*wx
�* 
dispw m   � ��)
�) stic    x �(yz
�( 
btnsy J   �{{ |}| m   �~~ �  C a n c e l} ��'� m  �� ���  C o n t i n u e�'  z �&��
�& 
dflt� m  
�� ���  C o n t i n u e� �%��$
�% 
htxt� m  �#
�# boovtrue�$  n o      �"�" 0 defaultanswer  l ��� r  '��� n  #��� 1  #�!
�! 
ttxt� o  � �  0 defaultanswer  � o      �� 0 x  � ��� l ((����  �  �  � ��� l ((����  �  �  � ��� l ((����  �   Encrypt Drive   � ���    E n c r y p t   D r i v e� ��� O  (V��� k  ,U�� ��� Z  ,S����� I ,4���
� .coredoexnull���     obj � 4  ,0��
� 
cdis� o  ./�� 0 u U�  � k  7O�� ��� l 77����  �  �  � ��� O  7M��� k  ;L�� ��� l ;;����  �  �  � ��� l ;;����  � < 6do shell script "sudo diskutil disableOwnership disk2"   � ��� l d o   s h e l l   s c r i p t   " s u d o   d i s k u t i l   d i s a b l e O w n e r s h i p   d i s k 2 "� ��� I ;J�
��	
�
 .sysoexecTEXT���     TEXT� b  ;F��� b  ;B��� m  ;>�� ��� P d i s k u t i l   c s   c o n v e r t   d i s k 2 s 2   - p a s s p h r a s e  � m  >A�� ���   � o  BE�� 0 x  �	  � ��� l KK����  �  �  �  � m  78���                                                                                      @ alis    <  Macintosh HD                   BD ����Terminal.app                                                   ����            ����  
 cu             	Utilities   &/:Applications:Utilities:Terminal.app/    T e r m i n a l . a p p    M a c i n t o s h   H D  #Applications/Utilities/Terminal.app   / ��  � ��� l NN��� �  �  �   �  �  �  � ���� l TT��������  ��  ��  ��  � m  ()���                                                                                  MACS  alis    @  Macintosh HD                   BD ����
Finder.app                                                     ����            ����  
 cu             CoreServices  )/:System:Library:CoreServices:Finder.app/    
 F i n d e r . a p p    M a c i n t o s h   H D  &System/Library/CoreServices/Finder.app  / ��  � ��� l WW��������  ��  ��  � ��� l WW������  � 2 , Display Window stating Encryption has begun   � ��� X   D i s p l a y   W i n d o w   s t a t i n g   E n c r y p t i o n   h a s   b e g u n� ��� I W^�����
�� .sysodlogaskr        TEXT� m  WZ�� ��� � Y o u r   U S B   D r i v e   i s   e n c r y p t i n g .   P l e a s e   r e m e m b e r   y o u r   c h o s e n   p a s s w o r d   t o   u n l o c k   d r i v e   f o r   f u t u r e   u s e��  � ��� l __��������  ��  ��  � ��� l __��������  ��  ��  � ���� l __������  �   End Encryption Check   � ��� *   E n d   E n c r y p t i o n   C h e c k��  �~  �}   � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ������  �   Multi Line Comment END    � ��� 0   M u l t i   L i n e   C o m m e n t   E N D  � ��� l     ������  �  *)   � ���  * )� ��� l     ������  � D >##############################################################   � ��� | # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #� ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ������  �   END OF FOLDER ACTION   � ��� *   E N D   O F   F O L D E R   A C T I O N� ��� l     ������  �   end adding folder items to   � ��� 4 e n d   a d d i n g   f o l d e r   i t e m s   t o� ���� l     ��������  ��  ��  ��       ������  � ��
�� .aevtoappnull  �   � ****� �����������
�� .aevtoappnull  �   � ****� k    `      -  =  N  j  �  �����  ��  ��  �  � 2�� 5 3�� F������ \�� Z���� t�� � ��� ��� � � � �!-26ISq��u������~�������������������
�� 
ascr
�� .sysoexecTEXT���     TEXT
�� 
curu
�� 
pnam�� 0 u U
�� 
cdis��  ��  �� 0 usbdata usbData�� $0 encryptionstatus encryptionStatus
�� .sysodlogaskr        TEXT
�� 
dtxt
�� 
disp
�� stic    
�� 
btns
�� 
dflt
�� 
htxt�� 
�� 0 defaultanswer  
�� 
ttxt�� 0 x  
�� .coredoexnull���     obj ��a�EkO� �j UO� 	*�,�,E�UO � 
�*��/�,FUW X  hO � 	�j E�UW X  hO � �a %j E` OPUOPW X  a j Oa E` O_ a   a j OhOPY �a j O�a   ;a j O� a j Oa j Oa j UO� �*�a /�,FUOPY a j OPOa a  a !a "a #a $a %a &lva 'a (a )ea * E` +O_ +a ,,E` -O� +*��/j . � a /a 0%_ -%j OPUOPY hOPUOa 1j OP ascr  ��ޭ