#!/usr/bin/env ruby
# Search text in first arugument with scan method
puts ARGV[0].scan(/^\d{10}$/).join
