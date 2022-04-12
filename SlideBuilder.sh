#!/bin/bash


#List of all projects and levels - we use this to loop through each directory (could probably do it programatically instead of hardcoded)
projects=("Bop_it" "Cryptography" "Flappy_Bird" "Guess_Who" "Markov_Chains" "Scissors_Paper_Rock" "Secret_Diary_Chatbot" "Tic_Tac_Toe")
levels=(g p n)


#We loop through each project that we have defined
for project in "${projects[@]}"
do
	#For each project, we have to go through each level
	for level in "${levels[@]}"
	do
		#We check if we have defined a slide instructions file for this project & level yet
		if [[ -f "$project/slide_instructions_$level.txt" ]]
		then
			#We remove the old slides and replace them with a blank file
			rm "$project"/slides_"$level".pdf
			touch "$project"/slides_"$level".pdf

			#We read the slide instructions and loop through each line, which corresponds to a PDF in the master slides directory
			input="$project/slide_instructions_$level.txt"
			while IFS= read -r line
			do
			  	echo "$line"
			  	#We copy each slide deck into our project directory
				cp Master_Slides/"$line".pdf "$project"

				#We merge those PDFs together into a new_slides PDF, which we then rename and delete (I haven't found a way to merge in place)
			  	gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE="$project"/new_slides_"$level".pdf -dBATCH "$project"/slides_"$level".pdf "$project"/"$line".pdf
			  	mv "$project"/new_slides_"$level".pdf "$project"/slides_"$level".pdf
			  	
			  	#We then delete the slide deck that we just merged in, leaving only the fully combined slides
			  	rm "$project"/"$line".pdf
			done < "$input"
		fi
	done
done


