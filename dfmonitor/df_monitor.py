#!/usr/bin/env python
"""
Copyright 2017 the original author or authors.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
"""
Monitor local Spring Cloud Dataflow app log
"""
import os, sys
from optparse import OptionParser

parser = OptionParser()

parser.usage = "%prog <app_log_dir> [options] --help for help"

parser.add_option('-l', '--less',

                  help='use less to read stdout log',
                  action='store_const',
                  const='less',
                  dest='mode')

parser.add_option('-u', '--url',
                  help='display app url info',
                  action='store_const',
                  const='url',
                  dest='mode')

parser.add_option('-i', '--instance',
                  type='int',
                  help='app instance number',
                  default=0,
                  dest='instance')

parser.add_option('-n', '--nlines',
                  type='int',
                  help='number of lines to tail, -f if not provided.',
                  default=0,
                  dest='lines')

def search_url_info(log_file_name):
    import re
    securityPattern = re.compile('.*Using default security password:\s+([\w-]+)')
    portPattern = re.compile('.*Tomcat started on .* (\d+)')
    url_info = {}
    with open(log_file_name) as log:
        for line in log:
            password = securityPattern.match(line)
            if (password):
                url_info['username'] = 'user'
                url_info['password'] = password.group(1)
            port = portPattern.match(line)
            if (port):
                #url_info['port'] = int(port.group(1))
                url_info['url'] = 'http://localhost:%d' %  int(port.group(1))

    print(url_info)
    return url_info

def build_command(args):

    options, arguments = parser.parse_args(args)

    if len(arguments) != 2:
        parser.print_usage()
        exit(1)

    log_file_name="%s/stdout_%d.log" % (arguments[1],options.instance)

    if (options.mode == 'url'):
        search_url_info(log_file_name)
        return None

    if options.mode == None:
        command = "tail -%s %s"
        if (options.lines == 0):
            command = command % ('f',log_file_name)
        else:
            command = command % (str(options.lines),log_file_name)


    elif (options.mode == 'less'):
            command="less %s" % log_file_name

    return command


def monitor(command):
    if (command == 'search'):
        print(search_url_info())


if __name__ == '__main__':
    command = build_command(sys.argv)

    if (command):
        os.system(command)
