#!/usr/bin/ruby

args = ARGV.sort { |a, b| a.to_i != b.to_i ? a.to_i <=> b.to_i : a <=> b }
args.each { |arg| puts arg }
