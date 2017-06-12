## Dataflow Monitor

A useful tool for working with local SCDF application logs.

```
Usage: dfmon <app_log_dir> [options]

Options:
  -h, --help            show this help message and exit
  -l, --less            use less to read stdout log
  -u, --url             display app url info
  -i INSTANCE, --instance=INSTANCE
                        app instance number
  -n LINES, --nlines=LINES
                        number of lines to tail, -f if not provided.
```


### Examples

```
2017-06-12 14:30:34.434  INFO 38870 --- [nio-9393-exec-6] o.s.c.d.spi.local.LocalAppDeployer       : Deploying app with deploymentId ticktock.log instance 0.
   Logs will be in /var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-877834982578906168/ticktock-1497292234306/ticktock.log
```

```
$dfmon /var/folders/hd/5yqz2v2d3sxd379f4sg4gr0000gn/T/spring-cloud-dataflow-877834982578906168/ticktock-1497292234306/ticktock.log
2017-06-12 14:32:30.408  INFO 22589 --- [time.ticktock-1] log-sink                                 : 06/12/17 14:32:30
2017-06-12 14:32:31.410  INFO 22589 --- [time.ticktock-1] log-sink                                 : 06/12/17 14:32:31
2017-06-12 14:32:32.413  INFO 22589 --- [time.ticktock-1] log-sink                                 : 06/12/17 14:32:32
...
```
$dfmon /var/folders/hd/5yqz2v2d3sxd379f4sg4gr0000gn/T/spring-cloud-dataflow-877834982578906168/ticktock-1497292234306/ticktock.log -u

{'username': 'user', 'url': 'http://localhost:60509', 'password': 'e8bff153-8901-4800-ad3e-d4e1c4ee9d66'}
```