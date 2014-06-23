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
    @frs = Frule.all
    respond_to do |format|
      format.html
      format.json{
        render :json => @frs.to_json
      }
    end
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
    respond_to do |format|
      format.html
      format.json{
        render :json => @brs.to_json
      }
    end
  end
  
  def bugreport
    @bug = Bugreport.where(:bid => params[:bid].to_i).first
    render :json => @bug.to_json
  end

  def login
  end

  def apply

  end

  def admission

  end

end