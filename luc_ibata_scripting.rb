#SRE scripting challenge week 1
# @lucibata

require 'find'
print "Enter directory name: "
directory_name = gets.chomp
Find.find(directory_name).each do |filefound|
	puts filefound	
end
