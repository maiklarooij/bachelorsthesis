import re
import pdfplumber

def create_metadata(form_data, files):

    # Create dict with data on request level
    metadata_dict = {k: v for k, v in form_data.to_dict().items() if v and not re.match(r'^doc[0-9]{1}.', k)}
    document_dict = {k: v for k, v in form_data.to_dict().items() if v and re.match(r'^doc[0-9]{1}.', k)}
    files_dict =  {k: v for k, v in files.to_dict().items()}

    prefix_set = set([name.split('.')[0] for name in document_dict])

    documents = []
    for number, document_prefix in enumerate(prefix_set):
        document_attributes = {k.replace(document_prefix+'.', ''): v for k, v in document_dict.items() if k.startswith(document_prefix)}
        document_attributes['identifier'] = f"{metadata_dict['identifier']}-{number+1}"

        try:
            refusal_grounds = document_attributes['groundsOfRefusal'].split(",")
            document_attributes['groundsOfRefusal'] = refusal_grounds
        except:
            pass

        document_attributes = enrich_document(files_dict[f"{document_prefix}.file"], document_attributes)
        documents.append(document_attributes)

    metadata_dict['documents'] = documents
    metadata_dict['numberDocuments'] = len(documents)

    return metadata_dict

def enrich_document(document_object, document_attributes):

    document_attributes['mimeType'] = document_object.mimetype
    document_attributes['fileName'] = document_object.filename

    if document_object.mimetype == 'application/pdf':

        with pdfplumber.open(document_object) as pdf:
            document_attributes['numberPages'] = len(pdf.pages)
    
    return document_attributes