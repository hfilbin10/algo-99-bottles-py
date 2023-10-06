def bottle_song():
	bottles = int(input("How many beers are you going to drink tonight?: "))

	while bottles > 2: # loop has to stop at 3 b/c "bottles" has to be singular in the second half of "2 bottles" lyric
		print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down and pass it around, {bottles - 1} bottles of beer on the wall.")
		bottles -= 1
	print(f"2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

print(bottle_song())

# * Make your code able to take in and account for any bottle amount
# * Refactor your code so it doesn't use any loops or iteration whatsoever

