class HomeController < ApplicationController
  layout "homelayout", except: [:login]
  def index
    @zone = 'index'
  end
  
  def fileupload
    @zone = 'fileupload'
  end
  
  def mbfunction
    @zone = 'mbfunction'
  end
  
  def frulecal
    @zone = 'frulecal'
  end
  
  def fruleview
    @zone = 'fruleview'
  end
  
  def mrmodel
    @zone = 'mrmodel'
  end
  
  def result
    @zone = 'result'
    @brs = Bugreport.paginate(:page => params[:page], :per_page => 20)
  end
  
  def bugreportview
    @zone = "bugreportview"
    @brs = Bugreport.paginate(:page => params[:page], :per_page => 20)
  end
  
  def login
  end

  def apply
    
  end
  
  def admission
     
  end
  
end