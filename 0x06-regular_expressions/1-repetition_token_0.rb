#!/usr/bin/env ruby
# Search text in first arugument with scan method
puts ARGV[0].scan(/hbt{2,5}n/).join
