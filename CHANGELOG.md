## v2.2.0 (2023-11-28)

- docker_ps: add bool option all to also list non running containers

## v2.1.2 (2023-11-21)

- docker_ps: fix bad indention of module return block

## v2.1.1 (2023-11-21)

- docker_ps: make option name_contains as not required

## v2.1.0 (2023-11-16)

- docker_ps: strip containers attributes
- docker_ps: add option name_contains to filter on container names

## v2.0.0 (2023-11-09)

- docker_ps: do not use json format output when executing `docker ps` command
- docker_ps: Use option `--no-trunc` when executing `docker ps` command
- docker_ps: change results key `names` (`ID` becomes `id`, `Names` becomes `name`, etc)

## v1.0.2 (2023-11-07)

- docker_ps: improve doc

## v1.0.1 (2023-10-30)

- Fix `docker` command `format` option
- Add CHANGELOG

## v1.0.0 (2023-10-28)

- Init release