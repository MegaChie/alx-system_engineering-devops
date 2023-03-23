#!/usr/bin/env ruby
# text
puts ARGV[0].scan(/\A\d{10}\z/).join
