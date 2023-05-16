#USB Encryption Check - Mac OS X 

#Detecting USB Drive through Folder Actions

[AppleScript]

--CHECKING VOLUMES FOLDER FOR DRIVE CHANGES (START OF FOLDER ACTION)


-- List all Drives in Volumes folder
tell application "Terminal"
	do shell script "ls /Volumes"
	
	
end tell

-- Check What Logical Drives Exist

set disk2s1Exists to ""
set disk2s2Exists to ""
set disk3s1Exists to ""
set disk3s2Exists to ""
set disk4s1Exists to ""
set disk4s2Exists to ""
set disk5s1Exists to ""
set disk5s2Exists to ""


tell application "Terminal"
	--DISK2
	set disk2s1Exists to do shell script "df -h | grep '/dev/disk2s1' | awk '{print $1}'"
	set disk2s2Exists to do shell script "df -h | grep '/dev/disk2s2' | awk '{print $1}'"
	--DISK3
	set disk3s1Exists to do shell script "df -h | grep '/dev/disk3s1' | awk '{print $1}'"
	set disk3s2Exists to do shell script "df -h | grep '/dev/disk3s2' | awk '{print $1}'"
	--DISK4
	set disk4s1Exists to do shell script "df -h | grep '/dev/disk4s1' | awk '{print $1}'"
	set disk4s2Exists to do shell script "df -h | grep '/dev/disk4s2' | awk '{print $1}'"
	--DISK5
	set disk5s1Exists to do shell script "df -h | grep '/dev/disk5s1' | awk '{print $1}'"
	set disk5s2Exists to do shell script "df -h | grep '/dev/disk5s2' | awk '{print $1}'"
end tell

--SETTING BOOLEAN VALUES
----------------------------------------------------------------------
--DISK2
if disk2s1Exists is not equal to "/dev/disk2s1" then
	set disk2s1Exists to false
else
	set disk2s1Exists to true
end if

if disk2s2Exists is not equal to "/dev/disk2s2" then
	set disk2s2Exists to false
else
	set disk2s2Exists to true
end if

--DISK3
if disk3s1Exists is not equal to "/dev/disk3s1" then
	set disk3s1Exists to false
else
	set disk3s1Exists to true
end if

if disk3s2Exists is not equal to "/dev/disk3s2" then
	set disk3s2Exists to false
else
	set disk3s2Exists to true
end if

--DISK4
if disk4s1Exists is not equal to "/dev/disk4s1" then
	set disk4s1Exists to false
else
	set disk4s1Exists to true
end if

if disk4s2Exists is not equal to "/dev/disk4s2" then
	set disk4s2Exists to false
else
	set disk4s2Exists to true
end if

--DISK5
if disk5s1Exists is not equal to "/dev/disk5s1" then
	set disk5s1Exists to false
else
	set disk5s1Exists to true
end if

if disk5s2Exists is not equal to "/dev/disk5s2" then
	set disk5s2Exists to false
else
	set disk5s2Exists to true
end if
------------------------------------------------------------------------


--DISK2 CHECK
if (disk2s1Exists is equal to true) or (disk2s2Exists is equal to true) then
	
	display dialog "External USB Mounted on /dev/disk2"
	set disk2Mounted to true
	
else
	display dialog "No USB Mounted on DISK2"
	set disk2Mounted to false
	
end if

--DISK3 CHECK
if (disk3s1Exists is equal to true) or (disk3s2Exists is equal to true) then
	
	display dialog "External USB Mounted on /dev/disk3"
	set disk3Mounted to true
	
else
	display dialog "No USB Mounted on DISK3"
	set disk3Mounted to false
	
end if

--DISK4 CHECK
if (disk4s1Exists is equal to true) or (disk4s2Exists is equal to true) then
	
	display dialog "External USB Mounted on /dev/disk4"
	set disk4Mounted to true
	
else
	display dialog "No USB Mounted on DISK4"
	set disk4Mounted to false
	
end if

--DISK5 CHECK
if (disk5s1Exists is equal to true) or (disk5s2Exists is equal to true) then
	
	display dialog "External USB Mounted on /dev/disk5"
	set disk5Mounted to true
	
else
	display dialog " No USB Mounted on DISK5"
	set disk5Mounted to false
	
end if
-------------------------------------------------------------------

--SEPARATING RENAMING LOGIC FROM SCRIPT TO AVOID LOOPING

(*

-- Set Variable to current username
tell application "System Events"
	set U to name of current user
end tell


-- Assign Each Disk Name to current username variable

--property ignoredVolumes : {"Macintosh HD", "Time Machine Backups"}

try
	tell application "Finder"
		set name of disk "KINGSTON" to U
		set name of disk "KINGSTON 1" to U
		set name of disk "KINGSTON 2" to U
		set name of disk "KINGSTON 3" to U
		
	end tell
end try

*)

--CHECK IF EACH DISK HAS DATA

--DISK2

if (disk2Mounted is equal to true) and (disk2s1Exists is equal to true) then
	
	try
		tell application "Terminal"
			
			set disk2Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk2s1' | awk '{print $3}'"
			
		end tell
	end try
	
else if (disk2Mounted is equal to true) and (disk2s1Exists is equal to false) then
	
	try
		tell application "Terminal"
			
			set disk2Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk2s2' | awk '{print $3}'"
			
		end tell
	end try
	
end if




--DISK3
if (disk3Mounted is equal to true) and (disk3s1Exists is equal to true) then
	
	try
		tell application "Terminal"
			
			set disk3Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk3s1' | awk '{print $3}'"
			
		end tell
	end try
	
else if (disk3Mounted is equal to true) and (disk3s1Exists is equal to false) then
	
	try
		tell application "Terminal"
			
			set disk3Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk3s2' | awk '{print $3}'"
			
		end tell
	end try
	
	
end if


--DISK4
if (disk4Mounted is equal to true) and (disk4s1Exists is equal to true) then
	
	try
		tell application "Terminal"
			
			set disk4Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk4s1' | awk '{print $3}'"
			
		end tell
	end try
	
else if (disk4Mounted is equal to true) and (disk4s1Exists is equal to false) then
	
	try
		tell application "Terminal"
			
			set disk4Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk4s2' | awk '{print $3}'"
			
		end tell
	end try
	
end if

--DISK5
if (disk5Mounted is equal to true) and (disk5s1Exists is equal to true) then
	
	try
		tell application "Terminal"
			
			set disk5Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk5s1' | awk '{print $3}'"
			
		end tell
	end try
	
else if (disk5Mounted is equal to true) and (disk5s1Exists is equal to false) then
	
	try
		tell application "Terminal"
			
			set disk5Data to do shell script "df -h /Volumes/" & U & " | grep '/dev/disk5s2' | awk '{print $3}'"
			
		end tell
	end try
	
end if


--display dialog usbData


-- Multi Line Comment START 
--(*

--CHECK IF DISK IS ENCRYPTED 
#################################################
--Check If Encryption is Completed

try
	set disk2s1LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk2s1' | awk '{print $3}'"
	set disk2s2LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk2s2' | awk '{print $3}'"
	set disk3s1LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk3s1' | awk '{print $3}'"
	set disk3s2LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk3s2' | awk '{print $3}'"
	set disk4s1LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk4s1' | awk '{print $3}'"
	set disk4s2LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk4s2' | awk '{print $3}'"
	set disk5s1LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk5s1' | awk '{print $3}'"
	set disk5s2LogicalDrive to do shell script "diskutil cs list | grep 'Disk:     disk5s2' | awk '{print $3}'"
	
	set disk2encryptionStatus to false
	set disk3encryptionStatus to false
	set disk4encryptionStatus to false
	set disk5encryptionStatus to false
	
	tell application "Terminal"
		
		if (disk2s1LogicalDrive is equal to "disk2s1") or (disk2s2LogicalDrive is equal to "disk2s2") then
			set disk2encryptionStatus to true
		end if
		
		if (disk3s1LogicalDrive is equal to "disk3s1") or (disk3s2LogicalDrive is equal to "disk3s2") then
			set disk3encryptionStatus to true
		end if
		
		if (disk4s1LogicalDrive is equal to "disk4s1") or (disk4s2LogicalDrive is equal to "disk4s2") then
			set disk4encryptionStatus to true
		end if
		
		if (disk5s1LogicalDrive is equal to "disk5s1") or (disk5s2LogicalDrive is equal to "disk5s2") then
			set disk5encryptionStatus to true
			
		end if
		
	end tell
	
	-- encryptionStatus variable value check
	--display dialog "Encryption Status:" & encryptionStatus
	
on error
	
	if disk2Mounted is equal to false then
		display dialog "The USB Device mounted on /dev/disk2 is not encrypted and can not securely store data"
	else
		set disk2encryptionStatus to true
		
	end if
	
	if disk3Mounted is equal to false then
		display dialog "The USB Device mounted on /dev/disk3 is not encrypted and can not securely store data"
	else
		set disk3encryptionStatus to true
		
	end if
	
	if disk4Mounted is equal to false then
		display dialog "The USB Device mounted on /dev/disk4 is not encrypted and can not securely store data"
	else
		set disk4encryptionStatus to true
		
	end if
	
	if disk5Mounted is equal to false then
		display dialog "The USB Device mounted on /dev/disk5 is not encrypted and can not securely store data"
	else
		set disk5encryptionStatus to true
		
	end if
	
	
end try


--If Encryption Status is Complete End Script

--DISK2
if (disk2encryptionStatus is equal to true) then
	display dialog "This USB Device on /dev/disk2 is Encrypted and can securely store data"
	return
	
else if (disk2encryptionStatus is equal to false) and (disk2Mounted is equal to true) then
	
	display dialog "Unencrypted USB Device detected, begining Encryption process for /dev/disk2.."
	
	--PROMPT FOR DISK2 PASSWORD
	
	-- Prompt for Encryption Password
	set defaultanswer to display dialog "Please create a password for this external drive." default answer "" with icon stop buttons {"Cancel", "Continue"} default button "Continue" with hidden answer
	set x to text returned of defaultanswer
	
	
	
	-- Encrypt Disk2
	
	--DISK2s1 ENCRYPTION
	if (disk2s1Exists is equal to true) then
		tell application "Finder"
			if disk U exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk2s1 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk2s1 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
	
	--DISK2s2 ENCRYPTION
	if (disk2s2Exists is equal to true) then
		tell application "Finder"
			if disk "KINGSTON" exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk2s2 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk2s2 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
end if
--END DISK2 ENCRYPTION	

--DISK3	
if (disk3encryptionStatus is equal to true) then
	display dialog "The USB Device on /dev/disk3 is Encrypted and can securely store data"
	return
	
else if (disk3encryptionStatus is equal to false) and (disk3Mounted is equal to true) then
	
	display dialog "Unencrypted USB Device detected, begining Encryption process for /dev/disk3.."
	
	
	--PROMPT FOR DISK3 PASSWORD
	
	-- Prompt for Encryption Password
	set defaultanswer to display dialog "Please create a password for this external drive." default answer "" with icon stop buttons {"Cancel", "Continue"} default button "Continue" with hidden answer
	set x to text returned of defaultanswer
	
	-- ENCRYPT DISK3
	
	--DISK3s1 ENCRYPTION
	if (disk3s1Exists is equal to true) then
		tell application "Finder"
			if disk "KINGSTON" exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk3s1 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk3s1 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
	
	--DISK3s2 ENCRYPTION
	if (disk3s2Exists is equal to true) then
		tell application "Finder"
			if disk "KINGSTON" exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk3s2 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk3s2 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
end if
--END DISK3 ENCRYPTION


--DISK4
if (disk4encryptionStatus is equal to true) then
	display dialog "The USB Device on /dev/disk4 is Encrypted and can securely store data"
	return
	
else if (disk4encryptionStatus is equal to false) and (disk4Mounted is equal to true) then
	
	display dialog "Unencrypted USB Device detected, begining Encryption process for /dev/disk4.."
	
	
	--PROMPT FOR DISK4 PASSWORD
	
	-- Prompt for Encryption Password
	set defaultanswer to display dialog "Please create a password for this external drive." default answer "" with icon stop buttons {"Cancel", "Continue"} default button "Continue" with hidden answer
	set x to text returned of defaultanswer
	
	
	
	--Encrypt Disk4
	
	--DISK4s1 ENCRYPTION
	if (disk4s1Exists is equal to true) then
		tell application "Finder"
			if disk "KINGSTON" exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk4s1 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk4s1 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
	
	
	--DISK4s2
	if (disk4s2Exists is equal to true) then
		tell application "Finder"
			if disk "KINGSTON" exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk4s2 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk4s2 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
end if
--END DISK4 ENCRYPTION

--DISK5
if (disk5encryptionStatus is equal to true) then
	display dialog "The USB Device on /dev/disk5 is Encrypted and can securely store data"
	return
	
else if (disk5encryptionStatus is equal to false) and (disk5Mounted is equal to true) then
	
	display dialog "Unencrypted USB Device detected, begining Encryption process for /dev/disk5.."
	
	
	--PROMPT FOR DISK5 PASSWORD
	
	-- Prompt for Encryption Password
	set defaultanswer to display dialog "Please create a password for this external drive." default answer "" with icon stop buttons {"Cancel", "Continue"} default button "Continue" with hidden answer
	set x to text returned of defaultanswer
	
	--Encrpyt Disk5
	
	--DISK5s1 ENCRYPTION
	if (disk5s1Exists is equal to true) then
		tell application "Finder"
			if disk "KINGSTON" exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk5s1 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk5s1 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
	
	--DISK5s2 ENCRYPTION
	if (disk5s2Exists is equal to true) then
		tell application "Finder"
			if disk "KINGSTON" exists then
				
				tell application "Terminal"
					--do shell script "sudo diskutil disableOwnership disk2"
					do shell script "diskutil cs convert disk5s2 -passphrase " & " " & x
					
				end tell
			end if
		end tell
		
		-- Display Window stating Encryption has begun
		display dialog "Your USB Drive mounted on /dev/disk5s2 is encrypting. Please remember your chosen password to unlock drive for future use"
	end if
end if
--END DISK5 ENCRYPTION





-- Set Variable to current username
tell application "System Events"
	set U to name of current user
end tell


-- Assign Each Disk Name to current username variable

--property ignoredVolumes : {"Macintosh HD", "Time Machine Backups"}

try
	tell application "Finder"
		set name of disk "KINGSTON" to U
		set name of disk "KINGSTON 1" to U
		set name of disk "KINGSTON 2" to U
		set name of disk "KINGSTON 3" to U
		
	end tell
end try











-- Reformat Disk to Journaled GUID Partition Table
-- Partition Disk

-- LOGIC TO DECIDE WHAT TO DO IF USB HAS DATA
#############################################
(*	
	if (disk2Data is equal to "111Mi") then
		
		display dialog "USB Device has no data, re-formatting drive"
		
		tell application "Terminal"
			do shell script "diskutil list"
			do shell script "diskutil eraseDisk JHFS+ KINGSTON GPT disk2"
			do shell script "diskutil partitionDisk disk2 GPT JHFS+ New 0b"
		end tell
		
		-- Assign Disk Name after Re-Format
		tell application "Finder"
			set name of disk "New" to U
		end tell
		
	else
		
		display dialog "USB Device has data, will not re-format drive"
		
		-- End Data Check
	end if
*)



(*	-- Assign Disk Name after Re-Format
		tell application "Finder"
			set name of disk "New" to U
		end tell *)





-- Multi Line Comment END 
--*)
###############################################################


-- END OF FOLDER ACTION
