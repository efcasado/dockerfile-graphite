Graphite Dockerfile
===================


### Build

```
make
```


### Usage

```
make start
```

```
make stop
```

> Note that if you are running Docker on OS X you will have to set up
> port forwarding from your OS X to the Docker host virtual machine.
> This can easily be done by running the following command:
>
> ```
> VBoxManage controlvm "<docker-host-name>" natpf1 "<pfrule-name>,tcp,,<local-port>,,<remote-port>"
> ```
>
> Note that the above command will only work if the Docker host
> virtual machine is running. If the machine is stopped, you can use
> this other command instead:
>
> ```
> VBoxManage modifyvm "<docker-host-name>" --natpf1 "<pfrule-name>,tcp,,<local-port>,,<remote-port>"
> ```


### How do I know it is working?

First, run `make start`, which will start a docker container running this
docker image. Once the docker container is running, you can open your
favourite web browser and go to `localhost:8080`. If the docker container
is running and properly configured you should be presented with Graphite's
web dashboard. You can try sending some dummy metrics using the following
code snippet:

```
echo "local.random.diceroll $RANDOM `date +%s`" | nc localhost 2003;
```

If everything is properly configured, you should see a new data point in
`Metrics -> local -> random -> diceroll`. Note that you might need
to shorten the period displayed in the graph in order to see the newly
generated data point.


### Ports

| Port Number | Protocol | Description                                                   |
|:-----------:|:--------:|---------------------------------------------------------------|
| 8080        | TCP      | Graphite web dashboard                                        |
| 2003        | TCP      | Feed in data to Graphite using the plain text protocol        |
| 2004        | TCP      | Feed in data to Graphite using the pickle protocol            |


### Author(s)

- Enrique Fernandez `<efcasado@gmail.com>`


### License

> The MIT License (MIT)
>
> Copyright (c) 2015 Enrique Fernandez
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.