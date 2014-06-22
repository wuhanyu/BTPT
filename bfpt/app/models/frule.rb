class Frule
  include Mongoid::Document
  include Mongoid::Timestamps
  field :fid
  field :pre
  field :cons
  field :conf
end