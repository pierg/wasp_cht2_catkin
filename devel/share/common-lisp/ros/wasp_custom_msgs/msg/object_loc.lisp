; Auto-generated. Do not edit!


(cl:in-package wasp_custom_msgs-msg)


;//! \htmlinclude object_loc.msg.html

(cl:defclass <object_loc> (roslisp-msg-protocol:ros-message)
  ((ID
    :reader ID
    :initarg :ID
    :type cl:fixnum
    :initform 0)
   (point
    :reader point
    :initarg :point
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (angles
    :reader angles
    :initarg :angles
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass object_loc (<object_loc>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <object_loc>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'object_loc)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wasp_custom_msgs-msg:<object_loc> is deprecated: use wasp_custom_msgs-msg:object_loc instead.")))

(cl:ensure-generic-function 'ID-val :lambda-list '(m))
(cl:defmethod ID-val ((m <object_loc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wasp_custom_msgs-msg:ID-val is deprecated.  Use wasp_custom_msgs-msg:ID instead.")
  (ID m))

(cl:ensure-generic-function 'point-val :lambda-list '(m))
(cl:defmethod point-val ((m <object_loc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wasp_custom_msgs-msg:point-val is deprecated.  Use wasp_custom_msgs-msg:point instead.")
  (point m))

(cl:ensure-generic-function 'angles-val :lambda-list '(m))
(cl:defmethod angles-val ((m <object_loc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wasp_custom_msgs-msg:angles-val is deprecated.  Use wasp_custom_msgs-msg:angles instead.")
  (angles m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <object_loc>) ostream)
  "Serializes a message object of type '<object_loc>"
  (cl:let* ((signed (cl:slot-value msg 'ID)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'angles) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <object_loc>) istream)
  "Deserializes a message object of type '<object_loc>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ID) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'angles) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<object_loc>)))
  "Returns string type for a message object of type '<object_loc>"
  "wasp_custom_msgs/object_loc")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'object_loc)))
  "Returns string type for a message object of type 'object_loc"
  "wasp_custom_msgs/object_loc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<object_loc>)))
  "Returns md5sum for a message object of type '<object_loc>"
  "7a1c2314593d80d85bf881c56f7c895d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'object_loc)))
  "Returns md5sum for a message object of type 'object_loc"
  "7a1c2314593d80d85bf881c56f7c895d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<object_loc>)))
  "Returns full string definition for message of type '<object_loc>"
  (cl:format cl:nil "#Custom message for publishing the detected object position~%#object_loc.msg~%int16 ID~%geometry_msgs/Point point~%geometry_msgs/Point angles~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'object_loc)))
  "Returns full string definition for message of type 'object_loc"
  (cl:format cl:nil "#Custom message for publishing the detected object position~%#object_loc.msg~%int16 ID~%geometry_msgs/Point point~%geometry_msgs/Point angles~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <object_loc>))
  (cl:+ 0
     2
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'angles))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <object_loc>))
  "Converts a ROS message object to a list"
  (cl:list 'object_loc
    (cl:cons ':ID (ID msg))
    (cl:cons ':point (point msg))
    (cl:cons ':angles (angles msg))
))
