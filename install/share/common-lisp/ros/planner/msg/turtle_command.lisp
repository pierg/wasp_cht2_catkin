; Auto-generated. Do not edit!


(cl:in-package planner-msg)


;//! \htmlinclude turtle_command.msg.html

(cl:defclass <turtle_command> (roslisp-msg-protocol:ros-message)
  ((turtle_id
    :reader turtle_id
    :initarg :turtle_id
    :type cl:string
    :initform "")
   (command
    :reader command
    :initarg :command
    :type cl:string
    :initform "")
   (posX
    :reader posX
    :initarg :posX
    :type cl:float
    :initform 0.0)
   (posY
    :reader posY
    :initarg :posY
    :type cl:float
    :initform 0.0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass turtle_command (<turtle_command>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <turtle_command>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'turtle_command)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name planner-msg:<turtle_command> is deprecated: use planner-msg:turtle_command instead.")))

(cl:ensure-generic-function 'turtle_id-val :lambda-list '(m))
(cl:defmethod turtle_id-val ((m <turtle_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-msg:turtle_id-val is deprecated.  Use planner-msg:turtle_id instead.")
  (turtle_id m))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <turtle_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-msg:command-val is deprecated.  Use planner-msg:command instead.")
  (command m))

(cl:ensure-generic-function 'posX-val :lambda-list '(m))
(cl:defmethod posX-val ((m <turtle_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-msg:posX-val is deprecated.  Use planner-msg:posX instead.")
  (posX m))

(cl:ensure-generic-function 'posY-val :lambda-list '(m))
(cl:defmethod posY-val ((m <turtle_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-msg:posY-val is deprecated.  Use planner-msg:posY instead.")
  (posY m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <turtle_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-msg:angle-val is deprecated.  Use planner-msg:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <turtle_command>) ostream)
  "Serializes a message object of type '<turtle_command>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'turtle_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'turtle_id))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'posX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'posY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <turtle_command>) istream)
  "Deserializes a message object of type '<turtle_command>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'turtle_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'turtle_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'posX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'posY) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<turtle_command>)))
  "Returns string type for a message object of type '<turtle_command>"
  "planner/turtle_command")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'turtle_command)))
  "Returns string type for a message object of type 'turtle_command"
  "planner/turtle_command")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<turtle_command>)))
  "Returns md5sum for a message object of type '<turtle_command>"
  "dd583d87765dc41b172179f34ec8aa3a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'turtle_command)))
  "Returns md5sum for a message object of type 'turtle_command"
  "dd583d87765dc41b172179f34ec8aa3a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<turtle_command>)))
  "Returns full string definition for message of type '<turtle_command>"
  (cl:format cl:nil "string turtle_id~%string command~%float32 posX~%float32 posY~%float32 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'turtle_command)))
  "Returns full string definition for message of type 'turtle_command"
  (cl:format cl:nil "string turtle_id~%string command~%float32 posX~%float32 posY~%float32 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <turtle_command>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'turtle_id))
     4 (cl:length (cl:slot-value msg 'command))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <turtle_command>))
  "Converts a ROS message object to a list"
  (cl:list 'turtle_command
    (cl:cons ':turtle_id (turtle_id msg))
    (cl:cons ':command (command msg))
    (cl:cons ':posX (posX msg))
    (cl:cons ':posY (posY msg))
    (cl:cons ':angle (angle msg))
))
