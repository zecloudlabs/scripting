#Begin Timer
beginning_time = Time.now
(1..10000).each { |i| i }
# by luc iBata aka Speed Matters  
# twitter @lucibata
# done 1 line or 6 lines

=begin
I  have a one liner but because it does not show hidder I am using the following code that iterates, 
using "do", looping through files found  by the "find" module.
I would pick the one liner just because it runs faster (performance)
=end

require 'find'
puts "Enter directory name"
directory_name = gets.chomp
Find.find(directory_name).each do |filefound|
	puts filefound	
end

#One liner code below
#puts Dir['**/*'] 

#End Timer
end_time = Time.now
puts "Time elapsed #{(end_time - beginning_time)*1000} milliseconds"
