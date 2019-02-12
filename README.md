# amara-quiz
amara kosha quiz application

- Code is based on docker-curriculum
- The underlying data come from https://github.com/sanskrit-coders/uohyd/tree/master/scl-master/amarakosha
  - amara_mulam.utf8 is forked from amara.utf8
  - amara_tokens*.utf8 is forked from all_kANdas

## Running locally via docker

- docker pull aupasana/amara-quiz (or clone this repo)
- docker build -t [aupasana/amara-quiz] .                 // Replace [] as appropriate
- docker run -p 8888:5000 [aupasana/amara-quiz]           // Replace [] as appropriate
