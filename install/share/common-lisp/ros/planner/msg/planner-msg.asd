
(cl:in-package :asdf)

(defsystem "planner-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "drone_command" :depends-on ("_package_drone_command"))
    (:file "_package_drone_command" :depends-on ("_package"))
    (:file "turtle_command" :depends-on ("_package_turtle_command"))
    (:file "_package_turtle_command" :depends-on ("_package"))
    (:file "drone_command" :depends-on ("_package_drone_command"))
    (:file "_package_drone_command" :depends-on ("_package"))
    (:file "turtle_command" :depends-on ("_package_turtle_command"))
    (:file "_package_turtle_command" :depends-on ("_package"))
  ))