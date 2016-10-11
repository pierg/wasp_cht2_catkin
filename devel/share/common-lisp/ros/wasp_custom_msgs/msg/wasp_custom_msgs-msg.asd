
(cl:in-package :asdf)

(defsystem "wasp_custom_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "image_point" :depends-on ("_package_image_point"))
    (:file "_package_image_point" :depends-on ("_package"))
    (:file "object_loc" :depends-on ("_package_object_loc"))
    (:file "_package_object_loc" :depends-on ("_package"))
  ))