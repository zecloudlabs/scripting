# by luc iBata aka Speed Matters  
# twitter @lucibata
# done 1 line or 6 lines

=begin
I  have a one liner but because it does not display hidden files, 
I am using the following code that iterates, 
using the "do" command, through files found  by the "find" module
=end

require 'find'
puts "Enter directory name"
directory_name = gets.chomp
Find.find(directory_name).each do |filefound|
	puts filefound	
end

#One liner
#puts Dir['**/*']
