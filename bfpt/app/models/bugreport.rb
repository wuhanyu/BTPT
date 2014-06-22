class Bugreport
  include Mongoid::Document
  include Mongoid::Timestamps
  field :bid
  field :seq
  field :resolution
  field :elapsedday
  field :commentnumber
  field :modinumber
  field :umodinumber
  field :attachnumber
  field :devnumber
  field :severity
  field :dependencynumber
  field :blocknumber
  field :reputation
  field :fsday
end