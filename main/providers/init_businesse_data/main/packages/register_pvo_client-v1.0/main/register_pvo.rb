
# ruby program to change service weight prob data stored in zk
# # contributed by qw0044! 2014-08-07!
#
require 'optparse'
require 'ostruct'
require 'mysql2'
require 'securerandom'
require 'json'

def reg_cli(host, username, password, name, type, url, dbname)
    client_id = SecureRandom.hex(10) + SecureRandom.random_number(10).to_s
    secret = SecureRandom.hex
    c = Mysql2::Client.new :host => host, :username => username,
        :password => password, :database => dbname
    c.query_options.merge!(:symbolize_keys => true)
    sql1 = "select * from pvo_clients where name = '#{name}' "
    sql1 += " and client_type = '#{type}' and callback_url = '#{url}'"
    r1 = c.query(sql1)
    if r1.count > 0
        JSON.generate :client_id => r1.first[:client_id]
    else
        sql2 = "insert into pvo_clients (name, client_type, "
        sql2 += " callback_url, client_id, secret) "
        sql2 += " values ('#{name}', '#{type}', '#{url}', "
        sql2 += "'#{client_id}', '#{secret}')"
        puts sql2
        c.query(sql2)
        client_id
        JSON.generate :client_id => client_id
    end
end

def show_usage(opts, msg)
      puts "### invalid usage: [#{msg}]"
      p opts
      exit(-1)
end

options = OpenStruct.new
options.host = "localhost"
options.username= "root" 
options.passwd= "magima.1"
options.name= ""
options.type= ""
options.url= ""
options.dbname="sysadmin"

opts = OptionParser.new
opts.on("--host HOST", "mysql host") do |arg|
    options.host = arg
end
opts.on("--username USERNAME", "mysql username") do |arg|
    options.username = arg
end
opts.on("--pwd PASSWORD", "mysql password") do |arg|
    options.passwd= arg
end
opts.on("--name NAME", "service name") do |arg|
    options.name = arg
end
opts.on("--type TYPE", "applicationt type(mobile,web,..)") do |arg|
    options.type = arg
end
opts.on("--url URL", "callback uri") do |arg|
    options.url = arg
end

def check_usage(opts, options)
    return "mysql server not set" if options.host == ""
    return "app type not set" if options.type == ""
    return "callback url not set" if options.url == ""
    return "ok"
end

opts.parse(ARGV)
usage_error_msg = check_usage(opts, options)
if usage_error_msg != "ok"
      show_usage(opts, usage_error_msg)
end

reg_cli(options.host, options.username, options.passwd, options.name, options.type,options.url,options.dbname)
        
#reg_cli("a","b","c","d","e","f","g")

exit(0)
