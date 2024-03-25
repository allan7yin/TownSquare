#!/bin/bash

function main {
  local env_name="$1"
  local command="$2"

  assert_env $env_name

  case "$command" in
    "migrate" )
      migrate "$env_name"
      ;;
    * )
      echoerr "invalid command: $command"
      ;;
    esac
}

function start {
  docker_compose "$1" "start"
}

function stop {
  docker_compose "$1" "stop"
}

function up {
  if [[ "$env_name" == "local" ]] #local env
  then
    docker_compose "$1" "up"
  else
    docker_compose "$1" "up --build -d"
  fi
}

function migrate {
  migration_message="$1"

  # Check if a message was provided
  if [[ -z "$migration_message" ]]; then
    echo "Error: Please provide a migration message as an argument."
    exit 1
  fi

  # Generate a new migration
  alembic revision -m "$migration_message"
  alembic upgrade head

  echo "Migrations applied successfully!"
}


env_name=$1
command=$2

main "$env_name" "$command"
